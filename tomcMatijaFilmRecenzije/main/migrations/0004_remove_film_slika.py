# Generated by Django 4.2.10 on 2024-02-18 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_film_slika'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='slika',
        ),
    ]
