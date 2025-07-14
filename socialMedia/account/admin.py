from django.contrib import admin
from .models import Relation, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ExtededUserAdmin(UserAdmin):
    inlines = [ProfileInline]
admin.site.unregister(User)
admin.site.register(User, ExtededUserAdmin)
admin.site.register(Relation)
admin.site.register(Profile)
