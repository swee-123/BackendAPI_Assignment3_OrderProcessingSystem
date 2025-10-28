import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, order_details):
    msg = MIMEMultipart()
    msg["From"] = os.getenv("SENDER_EMAIL")
    msg["To"] = to_email
    msg["Subject"] = f"Order Confirmation - {order_details.get('orderId')}"

    body = f"""
    Hello {order_details.get('customerEmail')},

    Your order for {order_details.get('item')} (Qty: {order_details.get('quantity')}) 
    has been received successfully.

    Thank you for shopping with us!
    """

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(os.getenv("MAILTRAP_HOST"), int(os.getenv("MAILTRAP_PORT"))) as server:
        server.login(os.getenv("MAILTRAP_USERNAME"), os.getenv("MAILTRAP_PASSWORD"))
        server.sendmail(msg["From"], msg["To"], msg.as_string())

    print(f"📤 Email sent successfully to {to_email}")
