from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Custom admin class for About model.

    This class specifies how the About model should
     be represented in the Django admin interface.
    It extends SummernoteModelAdmin to enable the
     Summernote WYSIWYG editor for the 'content' field.
    """

    summernote_fields = ('content',)
