# Generated by Django 3.0.8 on 2020-07-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0006_auto_20200719_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardsquare',
            name='column',
            field=models.CharField(max_length=1),
        ),
    ]
