# Generated by Django 2.2.5 on 2019-09-26 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0017_auto_20190922_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='deleted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='alias_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, default=False, related_name='alias_of', to='source_optics.Author'),
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['repo', 'path'], name='file3'),
        ),
        migrations.AddIndex(
            model_name='file',
            index=models.Index(fields=['repo', 'name', 'path', 'deleted'], name='file4'),
        ),
    ]
