from django.contrib import admin

# Register your models here.

from .models import Student, Subject, Marks

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Marks)