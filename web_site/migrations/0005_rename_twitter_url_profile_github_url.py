# Generated by Django 4.0.4 on 2022-05-25 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0004_alter_profile_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='twitter_url',
            new_name='github_url',
        ),
    ]