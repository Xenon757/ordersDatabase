from rest_framework import serializers
from .models import account, order


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ("id", "name", "email", "password")


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = (
            "id",
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
        )
