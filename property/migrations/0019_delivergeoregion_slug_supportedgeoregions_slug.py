# Generated by Django 5.0.6 on 2024-07-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_alter_delivergeoregion_region_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivergeoregion',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supportedgeoregions',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
