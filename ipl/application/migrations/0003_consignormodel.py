# Generated by Django 3.2 on 2021-12-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20211205_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsignorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('contact', models.BigIntegerField()),
                ('gstin', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('pincode', models.CharField(max_length=10)),
                ('created_dtm', models.DateTimeField(auto_now_add=True)),
                ('updated_dtm', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Consignor',
                'get_latest_by': 'created_dtm',
            },
        ),
    ]
