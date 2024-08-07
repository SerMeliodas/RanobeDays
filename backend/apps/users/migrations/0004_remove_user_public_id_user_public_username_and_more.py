# Generated by Django 5.0.3 on 2024-08-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_public_id_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='public_id',
        ),
        migrations.AddField(
            model_name='user',
            name='public_username',
            field=models.CharField(default='user', max_length=150, verbose_name='public username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='username'),
        ),
    ]
