from django.contrib import admin
from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'created_by', 'created_at', 'updated_at']
    search_fields = ['client_name']
    list_filter = ['created_by']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'client', 'created_by', 'created_at']
    search_fields = ['name']
    list_filter = ['client', 'created_by']
