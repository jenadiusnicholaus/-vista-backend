# Generated by Django 5.0.6 on 2024-07-25 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0040_alter_propertyrentingrequirements_options'),
        ('user_data', '0022_rename_canceled_myrentingstatus_renting_canceled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrenting',
            name='renting_duration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='property.propertyrentingdurationoptions'),
        ),
    ]