from django.contrib import admin
from .models import Background
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Background)
class BackgroundAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)