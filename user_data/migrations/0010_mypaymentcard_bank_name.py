# Generated by Django 5.0.6 on 2024-07-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0009_remove_mybookingpayment_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypaymentcard',
            name='bank_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]