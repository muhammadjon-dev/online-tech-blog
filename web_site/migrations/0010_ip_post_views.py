# Generated by Django 4.0.4 on 2022-06-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0009_alter_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='web_site.ip'),
        ),
    ]