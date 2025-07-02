
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import cv2
from gradcam import get_gradcam_overlay
from generate_pdf import generate_pdf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/lung_cancer_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if not os.path.exists('static'):
    os.makedirs('static')

db = SQLAlchemy(app)
model = load_model('model/lung_cancer_model.h5')
class_names = ['Benign', 'Malignant', 'Normal']

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
    prediction_result = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    pdf_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        class_idx = np.argmax(prediction)
        result = class_names[class_idx]
        confidence = prediction[0][class_idx] * 100

        heatmap_overlay = get_gradcam_overlay(model, img_array, filepath, class_idx)
        heatmap_path = os.path.join('static', 'heatmap.jpg')
        cv2.imwrite(heatmap_path, heatmap_overlay)

        patient_name = request.form.get('patient_name')
        pdf_path = os.path.join('static', f'{patient_name}_report.pdf')
        generate_pdf(patient_name, result, confidence, filepath, pdf_path)

        if result == 'Malignant':
            cancer_status = "⚠️ Important: The person is likely to have LUNG CANCER. Please consult a medical professional immediately."
            status_class = "text-danger"
        else:
            cancer_status = "✅ Good News: The person is NOT showing signs of lung cancer. Please continue regular health checkups."
            status_class = "text-success"

        new_patient = Patient(
            patient_name=patient_name,
            image_path=filepath,
            prediction_result=result,
            confidence=confidence,
            pdf_path=pdf_path
        )

        db.session.add(new_patient)
        db.session.commit()

        return render_template('result.html', result=result, confidence=confidence, img_path=filepath, heatmap_path=heatmap_path, pdf_path=pdf_path, cancer_status=cancer_status, status_class=status_class)

@app.route('/patients')
def patients():
    all_patients = Patient.query.order_by(Patient.created_at.desc()).all()
    return render_template('patients.html', patients=all_patients)

if __name__ == "__main__":
    app.run(debug=True)