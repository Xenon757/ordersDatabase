from django.db import models


class test(models.Model):
    name = models.CharField(max_length=50)
    spiceCount = models.IntegerField()

    def __str__(self):
        return self.name
