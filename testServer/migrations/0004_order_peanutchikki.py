# Generated by Django 4.2.7 on 2023-12-03 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testServer', '0003_rename_amount_order_besanladoo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='peanutChikki',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
