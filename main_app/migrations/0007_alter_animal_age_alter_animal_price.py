# Generated by Django 4.2.7 on 2023-11-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_animal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='animal',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
