# Generated by Django 3.2.12 on 2022-03-31 16:07

import apps.library.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_alter_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='participationapplicationfestival',
            name='festival_year',
            field=models.PositiveSmallIntegerField(default=apps.library.utilities.get_festival_year, verbose_name='Год фестиваля'),
        ),
    ]
