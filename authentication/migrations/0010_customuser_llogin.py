# Generated by Django 5.0.6 on 2024-07-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_verificationcode_otp_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='llogin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]