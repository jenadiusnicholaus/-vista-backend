# Generated by Django 5.0.6 on 2024-07-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_delivergeoregion_propertyasproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyasproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='propertyasproduct',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]