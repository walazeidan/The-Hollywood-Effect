# Generated by Django 3.2.8 on 2021-10-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adaptation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('synopsis', models.TextField(default=None, max_length=1000)),
                ('author', models.CharField(default=None, max_length=50)),
                ('book_release_year', models.PositiveIntegerField(default=None)),
                ('book_image', models.CharField(default=None, max_length=500)),
                ('director', models.CharField(default=None, max_length=50)),
                ('movie_release_year', models.PositiveIntegerField(default=None)),
                ('movie_image', models.CharField(default=None, max_length=500)),
                ('book_link', models.CharField(blank=True, max_length=500)),
                ('movie_link', models.CharField(blank=True, max_length=50)),
                ('genres', models.ManyToManyField(blank=True, related_name='adaptations', to='genres.Genre')),
            ],
        ),
    ]