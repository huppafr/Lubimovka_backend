# Generated by Django 3.2.7 on 2021-10-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_auto_20211007_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
    ]
