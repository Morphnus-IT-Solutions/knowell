from django.contrib import admin
from students.models import *

class StandardAdmin(admin.ModelAdmin):
    search_fields = ['standard']
    list_display = ('standard',)
admin.site.register(Standard, StandardAdmin)

class StreamAdmin(admin.ModelAdmin):
    search_fields = ['stream']
    list_display = ('stream',)
admin.site.register(Stream, StreamAdmin)

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']
    list_display = ('first_name', 'last_name', 'standard', 'phone_number', 'email', 'registration_number')
    list_filter = ('standard__standard',)
admin.site.register(Student, StudentAdmin)
