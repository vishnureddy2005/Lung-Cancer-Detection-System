CREATE DATABASE IF NOT EXISTS lung_cancer_db;

USE lung_cancer_db;

CREATE TABLE patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(255),
    image_path VARCHAR(255),
    prediction_result VARCHAR(50),
    confidence FLOAT,
    pdf_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
