from django.contrib import admin
from .models import test


class testAdmin(admin.ModelAdmin):
    list_display = ("name", "spiceCount")


# Register your models here.

admin.site.register(test, testAdmin)
