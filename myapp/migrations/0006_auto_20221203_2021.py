# Generated by Django 3.2.16 on 2022-12-03 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20221203_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 20, 21, 20, 350629)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 20, 21, 20, 350629)),
        ),
    ]
