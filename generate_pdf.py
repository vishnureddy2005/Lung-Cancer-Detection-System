from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from datetime import datetime
import qrcode

def generate_pdf(patient_name, result, confidence, image_path, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # 🏥 Hospital Logo (optional)
    logo_path = "D:\python_codes\hack\aits.png"  # Add your logo here if you want
    try:
        c.drawImage(logo_path, 50, height - 100, width=100, preserveAspectRatio=True, mask='auto')
    except:
        pass  # Skip if logo not found

    # 🕒 Timestamp (Top-right corner)
    c.setFont("Helvetica", 10)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawString(width - 200, height - 50, f"Generated: {timestamp}")

    # 📝 Centered Title
    c.setFont("Helvetica-Bold", 18)
    title = "Lung Cancer Detection Report"
    text_width = c.stringWidth(title, "Helvetica-Bold", 18)
    c.drawString((width - text_width) / 2, height - 100, title)

    # 📋 Patient Details
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, f"Patient Name: {patient_name}")
    c.drawString(100, height - 170, f"Prediction: {result}")
    c.drawString(100, height - 190, f"Confidence: {confidence:.2f}%")

    # 📂 X-ray Image
    c.drawImage(image_path, 100, height - 500, width=300, height=300)

    # 📝 Diagnosis Message
    c.setFont("Helvetica", 12)
    if result.lower() == "malignant":
        message = ("AI prediction indicates a malignant (cancerous) condition.\n"
                   "⚠️ This is not a confirmed medical diagnosis.\n"
                   "Please consult a medical professional immediately.")
    else:
        message = ("AI prediction indicates no lung cancer detected.\n"
                   "✅ This is not a confirmed medical diagnosis.\n"
                   "Please continue regular health checkups for your safety.")

    text_object = c.beginText(100, height - 520)
    for line in message.split('\n'):
        text_object.textLine(line)
    c.drawText(text_object)

    # 🔗 QR Code for Patient Records
    qr_link = "http://127.0.0.1:5000/patients"  # Update this if you deploy online
    qr = qrcode.make(qr_link)
    qr_path = f"static/{patient_name}_qr.png"
    qr.save(qr_path)

    c.drawImage(qr_path, 450, height - 500, width=100, height=100)
    c.setFont("Helvetica", 10)
    c.drawString(450, height - 510, "Scan to view records")

    c.save()
