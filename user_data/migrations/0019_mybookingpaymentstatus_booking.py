# Generated by Django 5.0.6 on 2024-07-25 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0018_alter_myaddress_options_alter_mybooking_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybookingpaymentstatus',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_data.mybooking'),
        ),
    ]
