# Generated by Django 2.2 on 2020-11-12 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_reads_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
