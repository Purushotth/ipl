# Generated by Django 3.2 on 2021-12-06 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_consignormodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drivermodel',
            options={'get_latest_by': 'created_dtm', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='ShippingOrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consignor_gst', models.CharField(max_length=15)),
                ('consignee_gst', models.CharField(max_length=15)),
                ('vehicle_no', models.CharField(max_length=45)),
                ('no_of_packages', models.CharField(max_length=15)),
                ('package_description', models.CharField(max_length=15)),
                ('actual_weight', models.CharField(max_length=15)),
                ('charged_weight', models.CharField(max_length=15)),
                ('invoice_no', models.CharField(max_length=45)),
                ('invoice_date', models.DateField()),
                ('invoice_amount', models.IntegerField()),
                ('gs_tax_payable', models.CharField(choices=[('Consignee', 'Consignee'), ('Consignor', 'Consignor'), ('IPL', 'IPL')], max_length=20)),
                ('created_dtm', models.DateTimeField(auto_now_add=True)),
                ('updated_dtm', models.DateTimeField(auto_now=True)),
                ('consignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.consigneemodel')),
                ('consignor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.consignormodel')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.drivermodel')),
            ],
            options={
                'db_table': 'LandingPage',
                'get_latest_by': 'created_dtm',
            },
        ),
    ]