# Generated by Django 3.0.6 on 2020-06-08 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcommFood', '0003_auto_20200608_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpdts',
            name='pdt',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='EcommFood.Products'),
        ),
    ]
