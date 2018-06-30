from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .models import FileUpload
from .form import UploadFileForm


class UploadFileCreate(CreateView):
    model = FileUpload
    form_class = UploadFileForm
    template_name = 'read_line/upload_file.html'
    success_url = reverse_lazy('read_files:upload_file')



