# Generated by Django 5.1 on 2024-09-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_cashier_employee_id_cashier_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocktransaction',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='stocktransaction',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stocktransaction',
            name='transaction_type',
            field=models.CharField(choices=[('sale', 'Sale'), ('restock', 'Restock')], max_length=10),
        ),
    ]