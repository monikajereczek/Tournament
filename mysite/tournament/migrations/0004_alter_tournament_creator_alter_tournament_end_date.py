# Generated by Django 4.0.5 on 2022-06-22 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0003_remove_tournament_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]
