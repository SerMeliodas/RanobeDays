# Generated by Django 5.0.3 on 2024-03-23 18:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0005_delete_chapter'),
        ('translator_teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TranslatorTeams',
            new_name='TranslatorTeam',
        ),
    ]
