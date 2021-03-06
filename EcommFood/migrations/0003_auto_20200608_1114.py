# Generated by Django 3.0.6 on 2020-06-08 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EcommFood', '0002_auto_20200607_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpdts',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orderpdts',
            name='price',
        ),
        migrations.AddField(
            model_name='orderpdts',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderpdts',
            name='pdt',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='EcommFood.Products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderpdts',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderpdts',
            name='qty',
            field=models.IntegerField(default='1'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('pdt', models.ManyToManyField(to='EcommFood.OrderPdts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
