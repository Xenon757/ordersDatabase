from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from testServer import views

router = routers.DefaultRouter()
router.register(r"accounts", views.accountView, "account")
router.register(r"orders", views.orderView, "order")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
