import smtplib
import mimetypes
from email.message import EmailMessage

def send_video(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL):
    print("Sending Video")
    message = EmailMessage()
    #sender = "kboysreel@gmail.com"
    #recipient = "inyangete@gmail.com"
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = 'INTRUDER ALERT'
    body = """Hello Client, 
    
    Activity has just been spotted, please find the video attached.
    
    Regards, 
    Your Raspberry!!!"""
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type('video/x-msvideo.avi')
    mime_type, mime_subtype = mime_type.split('/')
    with open(r"outpy.avi", 'rb') as file:
        message.add_attachment(file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename='record.avi')

    # print(message)
    mail_server =  smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    mail_server.set_debuglevel(0)
    mail_server.login(SENDER_EMAIL, SENDER_PASSWORD)
    mail_server.send_message(message)
    mail_server.quit()