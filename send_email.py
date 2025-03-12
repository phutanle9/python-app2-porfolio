import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message,email):
    # SMTP server details
    host = "smtp.gmail.com"
    port = 465
    # Login credentials
    username = "phutanle912@gmail.com"
    password = "teodnwfysinzupjs"
    # Receiver email address
    receiver = email

    # Create the message
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = "Test Email"

    # Attach the message (email body)
    msg.attach(MIMEText(message, "plain"))

    # Send the email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, msg.as_string())  # Convert message to string
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
