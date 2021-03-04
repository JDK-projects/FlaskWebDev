# %%
import smtplib
import os

usr = os.environ.get('MAIL_USERNAME')
pwd = os.environ.get('MAIL_PASSWORD')
# usr = 'joris.development@gmail.com'
# pwd = 'MyDevelopmentAccount'
print(f'User: {usr}, password: {pwd}')

# try:
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(usr, pwd)
# except ex:
#     print('Something went wrong')

# %%
import os

print(os.getcwd())

# %%

print(os.environ.get('MAIL_USERNAME'))


# %%
from flask_mail import Message
from app import mail

msg = Message('test subject', send=app.config['ADMINS'][0], recipients=['joris.software@gmail.com'])
