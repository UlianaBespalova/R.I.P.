# Generated by Django 2.2.6 on 2019-11-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20191103_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_question',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
    ]
