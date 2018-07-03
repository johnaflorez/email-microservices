from django.contrib import admin

from .models import FileUpload


@admin.register(FileUpload)
class AdminFileUpload(admin.ModelAdmin):
    list_display = ('archivo',)
