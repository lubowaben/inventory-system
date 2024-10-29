# Generated by Django 5.1 on 2024-08-28 11:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_cashier_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocktransaction',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='stocktransaction',
            name='transaction_type',
            field=models.CharField(max_length=20),
        ),
    ]
