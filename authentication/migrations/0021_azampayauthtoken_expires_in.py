# Generated by Django 5.0.6 on 2024-07-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_remove_azampayauthtoken_expires_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='azampayauthtoken',
            name='expires_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
