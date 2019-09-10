# Generated by Django 2.2.2 on 2019-09-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0004_statistic_commitment'),
    ]

    operations = [
        migrations.AddField(
            model_name='filechange',
            name='is_create',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filechange',
            name='is_edit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='filechange',
            name='is_move',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='creates',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='edits',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='moves',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
