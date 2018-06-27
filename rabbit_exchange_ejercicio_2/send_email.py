from django.conf import settings
from django.core.mail import EmailMessage

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


def enviar_email(subject, to, from_email, body):
    e = EmailMessage()
    e.subject = subject
    e.to = [to,]
    e.from_email = from_email
    e.body = body
    e.send()