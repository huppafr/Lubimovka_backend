# Generated by Django 3.2.11 on 2022-02-08 13:40

import apps.library.validators
from django.db import migrations, models

from apps.core.utils import slugify

def set_slug(apps, schema_editor):
    Author = apps.get_model("library", "Author")
    qs = Author.objects.all()
    for author in qs:
        if author.slug == "someslug":
            baseslug = slugify(author.person.last_name)
            used = qs.values_list("slug", flat=True)
            if baseslug in used:
                baseslug += str(author.person.id)
            author.slug = baseslug
            author.save()


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_play_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, default='someslug', help_text='Если не заполнено, будет сформировано автоматически', verbose_name='Транслит фамилии для формирования адресной строки'),
        ),
        migrations.AlterField(
            model_name='play',
            name='city',
            field=models.CharField(blank=True, max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, validators=[apps.library.validators.year_validator], verbose_name='Год написания пьесы'),
        ),
        migrations.RunPython(
            set_slug,
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, help_text='Если не заполнено, будет сформировано автоматически', unique=True, verbose_name='Транслит фамилии для формирования адресной строки'),
        ),
    ]
