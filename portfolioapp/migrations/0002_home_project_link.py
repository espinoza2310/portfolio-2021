# Generated by Django 3.2 on 2021-04-17 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='project_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]