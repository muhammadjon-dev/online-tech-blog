# Generated by Django 4.0.4 on 2022-05-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMaecenas tortor mauris, maximus nec ipsum euismod, auctor vehicula ipsum.\n'),
        ),
    ]
