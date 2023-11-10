# Generated by Django 4.2.7 on 2023-11-10 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='close_time',
            field=models.TimeField(help_text='24 hour format'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='coffee_rating',
            field=models.IntegerField(help_text='1-10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='open_time',
            field=models.TimeField(help_text='24 hour format'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='power_outlets',
            field=models.IntegerField(help_text='Number of power outlets available'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='wifi_rating',
            field=models.IntegerField(help_text='1-10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]