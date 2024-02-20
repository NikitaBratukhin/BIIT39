# Сгенерировано Django 12.11.2023

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(default='', max_length=30)),
                ('desc', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/%Y/%m/%d/')),
                ('views', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='blogs', to='blogs.category')),
            ],
        ),
        migrations.CreateModel(
            name='BlogLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likes', to='blogs.blog')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmarks', to='blogs.blog')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('published_on', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='blogs.blog')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('published_on', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='blogs.comment')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]