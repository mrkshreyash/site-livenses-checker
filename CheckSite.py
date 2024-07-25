import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests


def send_mail(subject: str, body: str):
    sender_mail: str = "sender-email-id"
    receiver_mail: str = "receiver-email-id"
    password: str = "sender-mail-security-key"

    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message['Subject'] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, message.as_string())


def check_site(url: str):
    subject: str = "Website Down Alert"

    response = requests.get(url, timeout=15)

    try:
        if (response.status_code == 200) or "your-existing-message (when site is live)" in response.text:
            print("Server is alive")

    except requests.Timeout:
        # body: str = f"Failed to check {url}. Error: {str(site_failed_error)}"
        # send_mail(subject, body)
        body: str = f"The website {url} is down ! HTTP Status Code: {str(response.status_code)}"
        send_mail(subject, body)
        print("Success: Sent Message")

    except requests.RequestException as e:
        subject = "Unnecessary error in server"
        print(f"Error: {str(e)}")
        body: str = f"Unnecessary error in connecting : {url}. HTTP Status Code: {str(response.status_code)}. Error: {str(e)}"
        send_mail(subject, body)


if __name__ == '__main__':
    website_url = "website-url-to-check-the-liveness"

    while True:
        try:
            check_site(website_url)
            time.sleep(300)  # 5 Minutes * 60 Seconds == 300 Seconds

        except Exception as checkout_failed_error:
            print(f"Error: {str(checkout_failed_error)}")
            print(f"Error: {str(checkout_failed_error)}")
