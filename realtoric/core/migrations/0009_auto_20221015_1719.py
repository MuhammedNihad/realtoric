# Generated by Django 3.2.15 on 2022-10-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='slug',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
