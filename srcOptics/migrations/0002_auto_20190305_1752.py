# Generated by Django 2.1.5 on 2019-03-05 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repository',
            old_name='lastScanned',
            new_name='last_scanned',
        ),
        migrations.RenameField(
            model_name='statistic',
            old_name='startDay',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='data',
        ),
        migrations.AddField(
            model_name='author',
            name='repos',
            field=models.ManyToManyField(related_name='author_repos', to='srcOptics.Repository'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='author_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='commit_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='files_changed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='lines_added',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='lines_changed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='lines_removed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='cred',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srcOptics.LoginCredential'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.TextField(blank=True, db_index=True, max_length=32),
        ),
    ]
