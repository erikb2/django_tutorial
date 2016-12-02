from django.contrib import admin

# Register your models here.
from .models import Job, candidate

admin.site.register(Job)
admin.site.register(candidate)