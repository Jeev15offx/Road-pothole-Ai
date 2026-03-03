import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from app.config import settings

def send_notification(latitude: float, longitude: float, confidence: float):

    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

    subject = "🚨 Pothole Detected - Immediate Attention Required"

    body = f"""
A pothole has been detected by the Road Pothole AI System.

Location:
Latitude: {latitude}
Longitude: {longitude}

Google Maps Link:
{maps_link}

Confidence Score: {confidence:.2f}

Detected At:
{datetime.now()}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_SENDER
    msg["To"] = settings.EMAIL_RECIPIENT

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
    server.sendmail(
        settings.EMAIL_SENDER,
        settings.EMAIL_RECIPIENT,
        msg.as_string()
    )
    server.quit()