import requests
import smtplib
from config import url2, rules, EMAIL_RECEIVER
from email.mime.text import MIMEText
import json


def get_data():
    is_respond = requests.get(url2)
    if is_respond.status_code == 200:
        data = json.loads(is_respond.text)
        return data

    return None


def archive_to_dir(filename, data):
    with open(f'directory/{filename}.json', 'w') as f:
        f.write(json.dumps(data))


def send_api_email(subject, text):
    text = json.dumps(text)


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'aslkd;alskdfaskjdf'
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login(';sdkfjlskdfljdf;sl', 'lkasdjflkjdf')
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        mail_server.quit()


# send email

def send_notification():
    pass


res = get_data()

if rules['archive']:
    archive_to_dir('tst1', res['data'])
