# Generated by Django 5.0.6 on 2024-07-24 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0012_alter_mypaymentcard_card_cvv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mypaymentcard',
            old_name='card_number',
            new_name='acount_number',
        ),
    ]
