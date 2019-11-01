import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pytilhan.utils.global_constant import g_send_email_id, g_send_email_password


# 메일 전송
def send_mail(to_email, subject, msg, email, password):
    
    mail_obj = MIMEMultipart("alternative")
    mail_obj['Subject'] = subject
    mail_obj['From'] = g_send_email_id
    mail_obj['To'] = to_email
    contents = MIMEText(msg, "html")
    mail_obj.attach( contents)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        
        smtp.login( email, password)
        smtp.sendmail( email , to_email, mail_obj.as_string() )


if __name__ == '__main__':

    send_mail("seungjin.han@chunlab.com","cccccccccc","<html><a href='#'>te한승진st</a>test </html>")