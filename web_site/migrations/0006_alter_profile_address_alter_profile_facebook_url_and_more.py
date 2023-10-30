# Generated by Django 4.0.4 on 2022-05-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0005_rename_twitter_url_profile_github_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='Uzbekistan', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, default='#', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, default='#', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, default='#', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, default='---------', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='---------', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telegram_url',
            field=models.CharField(blank=True, default='#', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, default='#', max_length=255),
        ),
    ]