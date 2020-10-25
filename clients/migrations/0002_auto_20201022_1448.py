# Generated by Django 2.2 on 2020-10-22 19:48

import clients.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='author',
        ),
        migrations.AlterField(
            model_name='client',
            name='acct_number',
            field=models.CharField(default=clients.models.random_string, max_length=50, null=True, verbose_name='Account Number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_address_city',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_address_line_1',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_address_line_2',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_address_state',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_address_zip',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='Zip'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_cell_phone',
            field=models.CharField(default=' ', max_length=50, null=True, verbose_name='Cell Phone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.EmailField(default=' ', max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_fname',
            field=models.CharField(default=' ', max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_lname',
            field=models.CharField(default=' ', max_length=50, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_vin', models.CharField(max_length=140, verbose_name='VIN Number')),
                ('vehicle_year', models.CharField(max_length=4, verbose_name='Year')),
                ('vehicle_make', models.CharField(max_length=50, verbose_name='Make')),
                ('vehicle_model', models.CharField(max_length=50, verbose_name='Model')),
                ('vehicle_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('service_amount', models.CharField(max_length=4, verbose_name='Amount')),
                ('service_details', models.CharField(max_length=140, verbose_name='Service Details')),
                ('service_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_record', to='clients.Vehicle')),
                ('vehicle_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_owner', to='clients.Client')),
            ],
        ),
    ]
