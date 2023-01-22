# Generated by Django 4.1.5 on 2023-01-22 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_eadmin'),
        ('eadmin', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='common.customer'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eadmin.product'),
        ),
    ]
