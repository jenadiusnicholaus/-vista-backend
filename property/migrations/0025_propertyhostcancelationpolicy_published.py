# Generated by Django 5.0.6 on 2024-07-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_property_contract_draft_delete_propertyforrent'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyhostcancelationpolicy',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]