# Generated by Django 5.0.2 on 2024-02-27 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0004_alter_novel_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chapter',
        ),
    ]
