# Generated by Django 2.2.6 on 2019-11-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20191125_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislike',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='likedislike',
            name='vote',
        ),
    ]
