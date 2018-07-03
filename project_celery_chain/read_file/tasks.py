from __future__ import absolute_import

from django.core.mail import EmailMessage
from celery import current_app
import os
from django.contrib.auth.models import User
import xlsxwriter


app = current_app


@app.task
def crear_archivo_xls():
    user = User.objects.filter(is_active=1)

    workbook = xlsxwriter.Workbook('media/usuario.xls', {'remove_timezone': True, 'default_date_format': 'dd/mm/yy'})
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "id")
    worksheet.write(0, 1, "last_login")
    worksheet.write(0, 2, "is_superuser")
    worksheet.write(0, 3, "username")
    worksheet.write(0, 4, "first_name")
    worksheet.write(0, 5, "last_name")
    worksheet.write(0, 6, "email")
    worksheet.write(0, 7, "is_staff")
    worksheet.write(0, 8, "is_active")
    worksheet.write(0, 9, "date_joined")

    for i, u in enumerate(user, start=1):
        worksheet.write(i, 0, u.id)
        worksheet.write(i, 1, u.last_login)
        worksheet.write(i, 2, u.is_superuser)
        worksheet.write(i, 3, u.username)
        worksheet.write(i, 4, u.first_name)
        worksheet.write(i, 5, u.last_name)
        worksheet.write(i, 6, u.email)
        worksheet.write(i, 7, u.is_staff)
        worksheet.write(i, 8, u.is_active)
        worksheet.write(i, 9, u.date_joined)

    workbook.close()

    return 'media/usuario.xls'


@app.task
def send_email(ruta):
    e = EmailMessage()
    e.subject = 'Reporte Usuarios'
    e.to = ['johnflorez_1289@hotmail.com', ]
    e.from_email = 'pruebadajngo@gmail.com'
    e.body = 'Anexo reporte en archivo xls'
    e.attach_file(ruta)
    e.send()

    return ruta


@app.task
def borra_archivo(ruta):
    os.remove(ruta)


@app.task(bind=True)
def reporte_usuario(self):
    (crear_archivo_xls.s() | send_email.s() | borra_archivo.s())()
