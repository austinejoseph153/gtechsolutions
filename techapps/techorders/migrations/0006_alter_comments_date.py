# Generated by Django 4.1.7 on 2023-03-08 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("techorders", "0005_alter_comments_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 8, 13, 25, 28, 891060)
            ),
        ),
    ]
