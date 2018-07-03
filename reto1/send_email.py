from django.conf import settings
from django.core.mail import EmailMessage
from celery import Celery

app = Celery('send_email', backend="amqp://guest:guest@localhost", broker="amqp://localhost")

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),

    EMAIL_USE_TLS=True,
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_HOST_USER='pruebadajngo@gmail.com',
    EMAIL_HOST_PASSWORD='pruebadjango123',
    EMAIL_PORT=587,
)

@app.task
def enviar_email(subject, to, from_email, type, code, message):
    if type == 'error':
        e = EmailMessage()
        e.subject = subject
        e.to = [to, ]
        e.from_email = from_email
        e.body = '\tType: {} \n\tCode: {} \n\tMessage: {}\n'.format(type, code, message)
        e.send()


@app.task
def crear_log(subject, to, from_email, type, code, message):
    archivo = '\nEmail Logs\n'
    archivo += 'Subject: {} \nFrom email: {} \n To: {} \n'.format(subject, to, from_email)
    archivo += 'Message: \n'
    archivo += '\tType: {} \n\tCode: {} \n\tMessage: {}\n'.format(type, code, message)
    archivo += '-' * 50

    file = open('logs.txt', 'a')
    file.write(archivo)
    file.close()


if __name__ == '__main__':
    subject = "Saludos"
    to = "johnflorez_1289@hotmail.com"
    from_email = "pruebadajngo@gmail.com"
    type = "error"
    code = "500"
    message = "error de servidor"

    crear_log.delay(subject, to, from_email, type, code, message)