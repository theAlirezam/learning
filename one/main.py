import requests
import json
import notification
from config import url2, rules
from khayyam import JalaliDate
from datetime import datetime

def get_data():
    is_respond = requests.get(url2)
    if is_respond.status_code == 200:
        data = json.loads(is_respond.text)
        return data

    return None


def archive_to_dir(filename, data):
    with open(f'directory/{filename}.json', 'w') as f:
        f.write(json.dumps(data))


"""
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

"""


def send_notification():
    notification.send_sms()


def check_notify():
    msg = ''
    i = int()
    for state in res['data']:
        if state['Slug State'] == rules['notification']['alert']:
            i += 1
    msg += f'{i}'

    return msg


res = get_data()

if rules['archive']:
    archive_to_dir(res['source'][0]['annotations']['table_id'], res['data'])

check = check_notify()
# if check == '':
#     raise ValueError('there is no alabama in states')
# else:
send_notification()
print(check)
now = datetime.today()
jnow = JalaliDate(now).strftime('%Y_%B-%A')
print(jnow)