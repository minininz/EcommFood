# Generated by Django 3.0.6 on 2020-06-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('typee', models.CharField(max_length=50)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]