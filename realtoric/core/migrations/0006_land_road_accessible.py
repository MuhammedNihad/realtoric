# Generated by Django 3.2.15 on 2022-10-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20221015_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='road_accessible',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20, verbose_name='Road Accessible'),
        ),
    ]
