# Generated by Django 2.2 on 2021-01-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]
