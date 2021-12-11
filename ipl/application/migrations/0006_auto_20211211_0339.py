# Generated by Django 3.2 on 2021-12-11 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20211210_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drivermodel',
            old_name='address',
            new_name='address_permanent',
        ),
        migrations.RemoveField(
            model_name='drivermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='drivermodel',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='drivermodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='drivermodel',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='drivermodel',
            name='state',
        ),
        migrations.AddField(
            model_name='drivermodel',
            name='address_temporary',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='drivermodel',
            name='alternate_contact',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='drivermodel',
            name='contact_number',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='drivermodel',
            name='date_of_joining',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='drivermodel',
            name='family_contact',
            field=models.BigIntegerField(default=None),
        ),
    ]
