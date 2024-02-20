# Generated by Django 3.2.10 on 2024-02-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djcms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='invite_events',
        ),
    ]