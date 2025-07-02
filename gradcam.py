import tensorflow as tf
import numpy as np
import cv2

def get_gradcam_overlay(model, img_array, original_image_path, class_idx):
    grad_model = tf.keras.models.Model([model.inputs], [model.get_layer('conv2d_1').output, model.output])

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        loss = predictions[:, class_idx]

    grads = tape.gradient(loss, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]

    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # Handle all-zero heatmap issue
    if tf.math.reduce_max(heatmap) == 0:
        heatmap = np.zeros_like(heatmap)
    else:
        heatmap = np.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)

    # Boost weak activations
    heatmap = heatmap ** 0.5  # Boost low intensity areas

    heatmap = cv2.resize(heatmap.numpy(), (224, 224))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    original_image = cv2.imread(original_image_path)
    original_image = cv2.resize(original_image, (224, 224))

    superimposed_img = cv2.addWeighted(original_image, 0.6, heatmap, 0.4, 0)

    return superimposed_img
