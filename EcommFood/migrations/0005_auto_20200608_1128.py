# Generated by Django 3.0.6 on 2020-06-08 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcommFood', '0004_auto_20200608_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderpdts',
            name='user',
        ),
    ]
