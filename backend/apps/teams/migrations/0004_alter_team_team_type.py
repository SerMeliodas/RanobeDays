# Generated by Django 5.0.3 on 2024-07-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_team_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_type',
            field=models.CharField(choices=[('A', 'Autor'), ('T', 'Translator')], default='A', max_length=1),
        ),
    ]
