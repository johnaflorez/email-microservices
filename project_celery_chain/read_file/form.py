from django import forms
from .models import FileUpload
from .tasks import crear_archivo_xls, send_email


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = [
            'archivo'
        ]

    def save(self, commit=True):
        file = super(UploadFileForm, self).save(commit=commit)

        (crear_archivo_xls.s() | send_email.s())()

        return file
