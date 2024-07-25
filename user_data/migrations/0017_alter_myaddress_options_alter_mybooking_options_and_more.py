# Generated by Django 5.0.6 on 2024-07-25 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0016_alter_myaddress_options_alter_mybooking_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myaddress',
            options={'verbose_name': '2. My Address', 'verbose_name_plural': '2. My Address'},
        ),
        migrations.AlterModelOptions(
            name='mybooking',
            options={'verbose_name': '5. My Booking', 'verbose_name_plural': '5. My Booking'},
        ),
        migrations.AlterModelOptions(
            name='mybookingpayment',
            options={'verbose_name': '7. Booking Payment', 'verbose_name_plural': '7. Booking Payment'},
        ),
        migrations.AlterModelOptions(
            name='mybookingpaymentstatus',
            options={'verbose_name': '8. Booking Payment Status', 'verbose_name_plural': '8. Booking Payment Status'},
        ),
        migrations.AlterModelOptions(
            name='mybookingstatus',
            options={'verbose_name': '6. Booking Status', 'verbose_name_plural': '6. Booking Status'},
        ),
        migrations.AlterModelOptions(
            name='myfavoriteproperty',
            options={'verbose_name': '1. My Favorite Property', 'verbose_name_plural': '1. My Favorite Property'},
        ),
        migrations.AlterModelOptions(
            name='mymobilemoneypaymentinfos',
            options={'verbose_name': '4. Mobile Money Payment ', 'verbose_name_plural': '4. Mobile Money Payment '},
        ),
        migrations.AlterModelOptions(
            name='mypaymentcard',
            options={'verbose_name': '3. My Payment Card', 'verbose_name_plural': '3. My Payment Card'},
        ),
        migrations.AlterModelOptions(
            name='mypropertypurchase',
            options={'verbose_name': '13. Property Purchase', 'verbose_name_plural': '13. Property Purchase'},
        ),
        migrations.AlterModelOptions(
            name='mypropertypurchasepayment',
            options={'verbose_name': '14. Purchase Payment', 'verbose_name_plural': '14. Purchase Payment'},
        ),
        migrations.AlterModelOptions(
            name='mypropertypurchasepaymentstatus',
            options={'verbose_name': '16. Purchase Payment Status', 'verbose_name_plural': '16. Purchase Payment Status'},
        ),
        migrations.AlterModelOptions(
            name='mypropertypurchasestatus',
            options={'verbose_name': '15. Purchase Status', 'verbose_name_plural': '15. Purchase Status'},
        ),
        migrations.AlterModelOptions(
            name='myrenting',
            options={'verbose_name': '9. Renting', 'verbose_name_plural': '9. Renting'},
        ),
        migrations.AlterModelOptions(
            name='myrentingpayment',
            options={'verbose_name': '10. Renting Payment', 'verbose_name_plural': '10. Renting Payment'},
        ),
        migrations.AlterModelOptions(
            name='myrentingpaymentstatus',
            options={'verbose_name': '12. Payment Status', 'verbose_name_plural': '12. Payment Status'},
        ),
        migrations.AlterModelOptions(
            name='myrentingstatus',
            options={'verbose_name': '11. Renting Status', 'verbose_name_plural': '11. Renting Status'},
        ),
    ]
