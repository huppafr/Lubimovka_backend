# Generated by Django 3.2.9 on 2021-11-21 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211103_0037'),
        ('core', '0009_add_description'),
        ('library', '0011_auto_20211118_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Член команды',
                'verbose_name_plural': 'Члены команды',
                'ordering': ('role',),
            },
        ),
        migrations.RemoveField(
            model_name='masterclass',
            name='host',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='director',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='dramatist',
        ),
        migrations.AddField(
            model_name='masterclass',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='masterclasses', to='articles.project', verbose_name='Проект'),
        ),
        migrations.AddField(
            model_name='performance',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performances', to='articles.project', verbose_name='Проект'),
        ),
        migrations.AddField(
            model_name='reading',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='readings', to='articles.project', verbose_name='Проект'),
        ),
        migrations.DeleteModel(
            name='PerformancePerson',
        ),
        migrations.AddField(
            model_name='teammember',
            name='masterclass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='library.masterclass', verbose_name='Мастер-класс'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='performance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='library.performance', verbose_name='Спектакль'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='core.person', verbose_name='Член команды'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='reading',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='library.reading', verbose_name='Читка'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='library.role', verbose_name='Роль'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='persons',
            field=models.ManyToManyField(related_name='masterclasses', through='library.TeamMember', to='core.Person', verbose_name='Члены команды'),
        ),
        migrations.AddField(
            model_name='reading',
            name='persons',
            field=models.ManyToManyField(related_name='readings', through='library.TeamMember', to='core.Person', verbose_name='Члены команды'),
        ),
        migrations.AddField(
            model_name='performance',
            name='persons',
            field=models.ManyToManyField(related_name='performances', through='library.TeamMember', to='core.Person', verbose_name='Члены команды'),
        ),
    ]
