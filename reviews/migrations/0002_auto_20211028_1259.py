# Generated by Django 3.2.8 on 2021-10-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie_rating',
        ),
        migrations.AddField(
            model_name='review',
            name='preference',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]