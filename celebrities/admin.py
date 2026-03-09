from django.contrib import admin
from celebrities.models import Celebrity, Category, Professions

# Register your models here.
admin.site.register (Celebrity)
admin.site.register (Category)
admin.site.register (Professions)