from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class account(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class order(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE, null=True)
    fullName = models.CharField(null=True, max_length=100)
    rasmalai = models.IntegerField(validators=[MinValueValidator(0)])
    kajuKatli = models.IntegerField(validators=[MinValueValidator(0)])
    chumChum = models.IntegerField(validators=[MinValueValidator(0)])
    peanutChikki = models.IntegerField(validators=[MinValueValidator(0)])
    besanLadoo = models.IntegerField(validators=[MinValueValidator(0)])
    dahiBhalla = models.IntegerField(validators=[MinValueValidator(0)])
    pindiChole = models.IntegerField(validators=[MinValueValidator(0)])
    stuffedKulcha = models.IntegerField(validators=[MinValueValidator(0)])
    gobhi = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField()
    status = models.BooleanField()
    progress = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], null=True
    )
    order_date = models.DateTimeField(auto_now_add=True)
