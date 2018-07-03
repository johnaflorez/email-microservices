from django.db import models


class FileUpload(models.Model):
    archivo = models.FileField(upload_to='files/')