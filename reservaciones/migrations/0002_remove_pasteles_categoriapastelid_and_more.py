# Generated by Django 5.0.1 on 2024-01-13 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasteles',
            name='CategoriaPastelID',
        ),
        migrations.DeleteModel(
            name='CategoriasPasteles',
        ),
        migrations.DeleteModel(
            name='Pasteles',
        ),
    ]