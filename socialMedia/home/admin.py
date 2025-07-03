from django.contrib import admin
from .models import Posts



class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'updated']
    search_fields = ['user', 'slug', 'body']
    list_filter = ['created', 'updated', 'slug']
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ['user']

admin.site.register(Posts, PostAdmin)
