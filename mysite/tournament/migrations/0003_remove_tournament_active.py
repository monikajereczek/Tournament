# Generated by Django 4.0.5 on 2022-06-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_rename_name_player_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='active',
        ),
    ]