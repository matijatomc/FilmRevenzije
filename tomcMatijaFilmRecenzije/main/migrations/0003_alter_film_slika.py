# Generated by Django 4.2.10 on 2024-02-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_film_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='slika',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
