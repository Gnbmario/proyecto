from django.contrib import admin
from app2.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_filter = ['age']
    search_fields = ['name']
    
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_filter = ['address']
    search_fields = ['name']



admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)

