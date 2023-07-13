from .. import mailsender
from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException

# def sendMail(to, subject):
#     msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     try:
#         msg.body = "Hola"
        
#         response = mailsender.send(msg)
        
#     except SMTPException as e:
#         print(e)
#         return "Entrega de correo fallida"
#     return True


#Ejemplo de chatgpt
def sendMail(to, subject, json_content):
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    try:
        # Renderizar el contenido del correo a partir del archivo de plantilla
        msg.body = render_template('email_template.txt', json_content=json_content)
        response = mailsender.send(msg)
        
    except SMTPException as e:
        print(e)
        return "Entrega de correo fallida"
    return True
