# Generated by Django 5.0.6 on 2024-07-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0036_remove_propertyhostcancelationpolicy_host_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '01. Category', 'verbose_name_plural': '01. Category'},
        ),
        migrations.AlterModelOptions(
            name='delivergeoregion',
            options={'verbose_name': '03. Deliver Geo Region', 'verbose_name_plural': '03. Deliver Geo Region'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': ' Properties', 'verbose_name_plural': ' Properties'},
        ),
        migrations.AlterModelOptions(
            name='supportedgeoregions',
            options={'verbose_name': '02. Supported Geo Region', 'verbose_name_plural': '02. Supported Geo Region'},
        ),
    ]
