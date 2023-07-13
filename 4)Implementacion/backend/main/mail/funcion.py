from .. import mailsender
from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException

def sendMail(to, subject, template, **kwargs):
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=to)
    try:
        msg.body = "Hola como andas?"
        response = mailsender.send(msg)
        
    except SMTPException as e:
        print(e)
        return "Entrega de correo fallida"
    return True