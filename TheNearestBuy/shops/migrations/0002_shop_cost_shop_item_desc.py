# Generated by Django 4.1.2 on 2022-10-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shop',
            name='item_desc',
            field=models.CharField(default='', max_length=100),
        ),
    ]
