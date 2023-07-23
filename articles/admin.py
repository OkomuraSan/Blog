from django import forms
from django.contrib import admin
from articles.models import ArticlesCategory, Articles
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Articles
        fields = '__all__'

@admin.register(ArticlesCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date', 'views',  )
    filter_horizontal = ["category"]
    form = ArticleAdminForm



