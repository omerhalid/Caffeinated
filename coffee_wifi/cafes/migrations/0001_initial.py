# Generated by Django 4.2.7 on 2023-11-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.URLField()),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('coffee_rating', models.IntegerField()),
                ('wifi_rating', models.IntegerField()),
                ('power_outlets', models.IntegerField()),
            ],
        ),
    ]
