from django.contrib import admin
from .models import Background, TestimonialRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Background)
class BackgroundAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(TestimonialRequest)
class TestimonialRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)