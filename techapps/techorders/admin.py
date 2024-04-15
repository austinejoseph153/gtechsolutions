from django.contrib import admin
from .models import Testimonials, Contact
from .models import (ProjectUpload)

@admin.register(ProjectUpload)
class ProjectsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':(
                ('file_name'),
                ('img_url'),
            )
        }),
    )
    list_display = ('pk','file_name',)
    list_filter = ('file_name',)

@admin.register(Testimonials)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':(
                ('firstname', 'lastname', 'email'),
                ('review'),
            )
        }),
    )
    list_display = ('pk','firstname','lastname','email', 'date')
    list_filter = ('date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':(
                ('firstname', 'lastname', 'email', 'phone'),
                ('message'),
            )
        }),
    )
    list_display = ('pk', 'firstname', 'lastname', 'email', 'phone', 'date')
    list_filter = ('date',)


