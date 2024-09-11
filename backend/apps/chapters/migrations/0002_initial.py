# Generated by Django 5.0.3 on 2024-09-11 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapters', '0001_initial'),
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='novel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novels.novel'),
        ),
    ]