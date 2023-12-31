# Generated by Django 4.2.7 on 2023-11-26 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testServer', '0002_account_order_delete_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount',
            new_name='besanLadoo',
        ),
        migrations.RemoveField(
            model_name='order',
            name='foodOrder',
        ),
        migrations.AddField(
            model_name='order',
            name='chumChum',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='dahiBhalla',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='gobhi',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='kajuKatli',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='pindiChole',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='rasmalai',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='stuffedKulcha',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
