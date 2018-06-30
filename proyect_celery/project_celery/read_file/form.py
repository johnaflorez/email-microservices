from django import forms
from .models import FileUpload
from .tasks import upload_name_file


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = [
            'archivo'
        ]

    def save(self, commit=True):
        file = super(UploadFileForm, self).save(commit=commit)
        upload_name_file.delay(file.pk)
        return file
