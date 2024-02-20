# Generated by Django 3.2.10 on 2024-02-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djcms', '0004_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]