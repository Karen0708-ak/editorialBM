# Generated by Django 5.2 on 2025-05-27 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='Libreria',
            new_name='libreria',
        ),
    ]
