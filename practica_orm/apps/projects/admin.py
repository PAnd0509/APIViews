from django.contrib import admin
from .models import *
from apps.users.models import *
# Registerc your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=["name","init_date","end_date"]

class TaskAdmin(admin.ModelAdmin):
    list_display=["id", "description","project","end_date"]

class CommentAdmin(admin.ModelAdmin):
    list_display=["id","task", "content","init_date"]

class MemberAdmin(admin.ModelAdmin):
    list_display=["id","user", "project","rol","date"]

class OwnerAdmin(admin.ModelAdmin):
    list_display=["id","user", "task"]

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Owner,OwnerAdmin)