# Generated by Django 3.2 on 2021-04-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20210410_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='last_date',
            field=models.DateTimeField(null=True, verbose_name='Son Tarihi'),
        ),
    ]
