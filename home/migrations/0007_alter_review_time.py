# Generated by Django 4.1.3 on 2022-12-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
