# Generated by Django 4.0.1 on 2022-02-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.CharField(default='time', max_length=30),
        ),
    ]