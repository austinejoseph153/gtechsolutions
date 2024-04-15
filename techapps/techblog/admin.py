from django.contrib import admin, messages
from ckeditor.widgets import CKEditorWidget
from django import forms
from techapps.techblog.models import PostField, Tag, Comment

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = PostField
        fields = ['title','slug','author','thumbnail','content','read_time','tags','is_public']
        widgets = {
            'content': CKEditorWidget()
        }


@admin.register(PostField)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    
    fieldsets = (
        (None, {
            'fields': (('title','slug',),
                       ('thumbnail','read_time','is_public'),
                       ('author','tags'),
                       ('content'),
                       )
        }),
    )
    
    summernote_fields = ('content',)
    raw_id_fields = ['author', 'tags']
    list_display = ('id','title', 'is_public', 'slug',
                     'created_at', 'edited_at',)
    list_filter = ('is_public', 'created_at', 'edited_at',)
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_public', 'make_unpublic']

    def make_public(self, request, queryset):
        queryset.update(is_public=True)
        messages.success(
            request, 'Selected Post(s) are now public !')

    def make_unpublic(self, request, queryset):
        queryset.update(is_public=False)
        messages.success(
            request, 'Selected Post(s) are no longer public!')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'id', 'post',
                    'author', 'created_at')
    search_fields = ['author', 'body']
    list_filter = ('created_at',)