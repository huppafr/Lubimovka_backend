# Generated by Django 3.2.9 on 2021-11-29 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20211127_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='programtype',
            name='slug',
            field=models.SlugField(default=1, max_length=40, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
