# Generated by Django 3.2.10 on 2022-01-02 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]