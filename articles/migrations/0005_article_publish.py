# Generated by Django 3.2.10 on 2022-01-02 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20220102_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]