# Generated by Django 2.2.5 on 2019-09-18 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0011_auto_20190918_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='repos',
        ),
        migrations.RemoveField(
            model_name='repository',
            name='tags',
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['author', 'repo'], name='commit3'),
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['author'], name='commit4'),
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['repo'], name='commit5'),
        ),
        migrations.AddIndex(
            model_name='emailalias',
            index=models.Index(fields=['organization', 'from_email'], name='email_alias1'),
        ),
        migrations.AddIndex(
            model_name='repository',
            index=models.Index(fields=['organization', 'enabled'], name='source_opti_organiz_45e49d_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['start_date', 'interval', 'repo'], name='author_rollup4'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['start_date', 'interval', 'author'], name='author_rollup5'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
