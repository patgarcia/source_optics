# Generated by Django 2.0.10 on 2019-02-18 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0009_filechange_ext'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='files',
            field=models.ManyToManyField(related_name='files', to='srcOptics.FileChange'),
        ),
        migrations.AddField(
            model_name='filechange',
            name='path',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='filechange',
            name='commit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commit', to='srcOptics.Commit'),
        ),
        migrations.AlterField(
            model_name='filechange',
            name='name',
            field=models.TextField(max_length=256, null=True),
        ),
    ]