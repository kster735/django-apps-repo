# Generated by Django 5.0.7 on 2024-07-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_imdb_plot'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='year',
            field=models.IntegerField(default=1980),
            preserve_default=False,
        ),
    ]
