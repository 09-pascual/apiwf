# Generated by Django 5.1.2 on 2024-11-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapiapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='group',
            name='workers',
        ),
        migrations.AddField(
            model_name='project',
            name='groups',
            field=models.ManyToManyField(related_name='groups', through='workflowapiapi.ProjectGroup', to='workflowapiapi.group'),
        ),
    ]
