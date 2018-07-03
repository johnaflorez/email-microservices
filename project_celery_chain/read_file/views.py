from django.shortcuts import render
from .tasks import crear_archivo_xls, send_email, borra_archivo


def index(request):
    if request.method == 'POST':
        (crear_archivo_xls.s() | send_email.s() | borra_archivo.s())()
    return render(request, 'read_line/index.html')
