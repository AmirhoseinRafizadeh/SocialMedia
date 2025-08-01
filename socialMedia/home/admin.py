from django.contrib import admin
from .models import Posts, comments, Vote



class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'updated']
    search_fields = ['user', 'slug', 'body']
    list_filter = ['created', 'updated', 'slug']
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ['user']

admin.site.register(Posts, PostAdmin)

class commentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'body', 'created']
    raw_id_fields = ['user', 'post', 'reply']
admin.site.register(comments, commentsAdmin)

admin.site.register(Vote)