🩺 Lung Cancer Detection System

This project is a Lung Cancer Detection Web Application using Deep Learning and Flask. The system allows users to upload lung CT scan images, predicts the presence of lung cancer, provides Grad-CAM visualizations to explain the model’s decision, and automatically generates a PDF report for each prediction.

📌 Key Features

✅ Lung cancer detection using a trained Convolutional Neural Network (CNN).

✅ Grad-CAM visualization to highlight cancerous regions.

✅ Automatic PDF report generation.

✅ Clean and interactive Flask web interface.

✅ Dataset preprocessing and model training scripts included.

✅ Database integration for storing patient and prediction records.


🛠️ Technologies Used

1.Python

2.Flask (Web framework)

3.TensorFlow / Keras (Deep Learning)

4.OpenCV (Image Processing)

5.Grad-CAM (Model explainability)

6.SQLite (Database)

7.PDFKit / ReportLab (PDF generation)

8.HTML, CSS (Frontend)


📦 Project Structure

Lung Cancer Detection Project/
│
├── app.py                  # Main Flask app
├── train_model.py          # Model training script
├── gradcam.py              # Grad-CAM visualization
├── generate_pdf.py         # PDF report generator
├── split_dataset.py        # Dataset splitting script
│
├── model/                  # Trained model files
├── dataset/                # Preprocessed dataset
├── lung_cancer/            # Lung cancer image processing
├── The IQ-OTHNCCD lung cancer dataset/   # Original dataset
├── Test cases/             # Test images
├── static/                 # Static files (CSS, JS, Images)
├── templates/              # HTML templates for Flask
└── requirements.txt        # Python dependencies


🚀 Running the Project

1.Train the model :  python train_model.py

2.Start the Flask server:python app.py

3.Open your browser and go to:http://127.0.0.1:5000/



📚 Dataset Details

-Dataset Name: The IQ-OTH/NCCD Lung Cancer Dataset

-Contains lung CT scan images categorized for lung cancer detection.

-Dataset is split into training, testing, and validation using split_dataset.py.

🔥 Grad-CAM (Heatmap) Visualization

What is Grad-CAM?

Grad-CAM (Gradient-weighted Class Activation Mapping) is used to generate heatmaps that highlight the regions of the CT scan image that strongly influenced the model’s prediction.

Workflow:

1.Upload CT scan image via Flask web app.

2.Model predicts the result (Cancer / No Cancer).

3.Grad-CAM generates a heatmap to highlight critical areas.

4.Heatmap is overlaid on the original image.

5.The final heatmap is displayed in the web interface and included in the PDF report.

Heatmap Example in Flask:

from gradcam import generate_gradcam, overlay_heatmap

# Generate heatmap
heatmap = generate_gradcam(model, processed_image, 'last_conv_layer_name')

# Overlay heatmap on original image
overlay_image = overlay_heatmap(uploaded_image_path, heatmap)



📄 PDF Report Generation

-After each prediction, a PDF report is automatically generated using PDFKit or ReportLab.

-The report contains:

1.Patient Name

2.Uploaded Image

3.Prediction Result

4.Grad-CAM Visualization

5.Prediction Timestamp


✅ Python Packages Used

Flask               # Web application framework
TensorFlow          # Deep learning model
OpenCV              # Image processing
NumPy               # Numerical operations
Pillow              # Image handling
Matplotlib          # Visualization (Grad-CAM)
Pandas              # Data handling (optional)
ReportLab           # PDF report generation
PDFKit              # PDF file creation (optional)
SQLite3             # Database (built-in with Python)


👨‍💻 Author

Vishnu Vardhan Reddy
Computer Science Engineer | AI Enthusiast




