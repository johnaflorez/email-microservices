from __future__ import absolute_import

import os

import xlrd
from celery import current_app
from django.contrib.auth.models import User

from .models import FileUpload

app = current_app


@app.task
def upload_name_file(id):
    f = FileUpload.objects.get(pk=id)

    archivo, extension = os.path.splitext(f.archivo.path)

    if extension == '.xls':
        try:
            wb2 = xlrd.open_workbook(f.archivo.path)
            sheet = wb2.sheet_by_index(0)

            lista = [0] * sheet.ncols

            for r in range(1, sheet.nrows):
                for c in range(0, sheet.ncols):
                    lista[c] = sheet.cell_value(r, c)
                User.objects.create(
                    id=lista[0],
                    last_login=lista[1],
                    is_superuser=lista[2],
                    username=lista[3],
                    first_name=lista[4],
                    last_name=lista[5],
                    email=lista[6],
                    is_staff=lista[7],
                    is_active=lista[8],
                    date_joined=lista[9]
                )

        except Exception as e:
            print(f.archivo.name)
    else:
        print(f.archivo.name)
