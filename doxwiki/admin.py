from django.contrib import admin
from .models import *


class AttachmentInline(admin.TabularInline):
    model = Attachment


class PageAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]


# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Attachment)

