from django.contrib import admin

from .models import account, order


class accountAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password")


class orderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "fullName",
        "rasmalai",
        "kajuKatli",
        "chumChum",
        "peanutChikki",
        "besanLadoo",
        "dahiBhalla",
        "pindiChole",
        "stuffedKulcha",
        "gobhi",
        "price",
        "status",
        "progress",
        "order_date",
    )


# Register your models here.

admin.site.register(account, accountAdmin)
admin.site.register(order, orderAdmin)
