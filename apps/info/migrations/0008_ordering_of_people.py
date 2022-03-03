# Generated by Django 3.2.12 on 2022-02-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_renaming_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='festivalteammember',
            options={'ordering': ('person__last_name', 'person__first_name'), 'verbose_name': 'Команда фестиваля', 'verbose_name_plural': 'Команды фестиваля'},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'ordering': ('person__last_name', 'person__first_name'), 'verbose_name': 'Волонтёр фестиваля', 'verbose_name_plural': 'Волонтёры фестиваля'},
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(help_text='Загрузите логотип партнёра', upload_to='images/info/partnerslogo', verbose_name='Логотип'),
        ),
    ]
