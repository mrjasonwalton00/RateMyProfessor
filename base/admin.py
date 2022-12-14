from django.contrib import admin
from .models import Professor, Review, Subject, Courses

# Register your models here.
admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(Subject)
admin.site.register(Courses)
