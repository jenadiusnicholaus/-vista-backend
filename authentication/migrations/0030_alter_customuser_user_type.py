# Generated by Django 5.0.6 on 2024-12-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0029_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('guest', 'Guest'), ('host', 'Host')], default='geust', max_length=255),
        ),
    ]
