from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course_interest', 'status', 'created_at']
    list_filter = ['course_interest', 'status']
    search_fields = ['name', 'email']
    list_editable = ['status']
    ordering = ['-created_at']
