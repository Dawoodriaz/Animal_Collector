# Generated by Django 4.2.7 on 2023-11-07 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_animal_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toy',
            new_name='Country',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='toys',
            new_name='countries',
        ),
    ]
