# Generated by Django 5.0.3 on 2024-07-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0002_alter_chapter_options_chapter_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='chapter',
            name='volume',
            field=models.IntegerField(default=1),
        ),
    ]
