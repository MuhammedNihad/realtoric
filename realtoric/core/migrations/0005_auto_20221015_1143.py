# Generated by Django 3.2.15 on 2022-10-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20221006_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='car_parking',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='carpet_area',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='construction_status',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='furnishing',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='listed_by',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='no_of_balcony',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='rent_status',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='sell_or_rent',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='society_amenity',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='super_built_up_area',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='carpet_area',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='construction_status',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='furnishing',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='listed_by',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='rent_status',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='sell_or_rent',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='super_built_up_area',
        ),
        migrations.RemoveField(
            model_name='commercial',
            name='washrooms',
        ),
        migrations.RemoveField(
            model_name='house',
            name='car_parking',
        ),
        migrations.RemoveField(
            model_name='house',
            name='carpet_area',
        ),
        migrations.RemoveField(
            model_name='house',
            name='construction_status',
        ),
        migrations.RemoveField(
            model_name='house',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='house',
            name='furnishing',
        ),
        migrations.RemoveField(
            model_name='house',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='house',
            name='listed_by',
        ),
        migrations.RemoveField(
            model_name='house',
            name='rent_status',
        ),
        migrations.RemoveField(
            model_name='house',
            name='sell_or_rent',
        ),
        migrations.RemoveField(
            model_name='house',
            name='super_built_up_area',
        ),
        migrations.RemoveField(
            model_name='land',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='land',
            name='rent_status',
        ),
        migrations.RemoveField(
            model_name='land',
            name='sell_or_rent',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='car_parking',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='carpet_area',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='construction_status',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='furnishing',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='listed_by',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='rent_status',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='sell_or_rent',
        ),
        migrations.RemoveField(
            model_name='villa',
            name='super_built_up_area',
        ),
        migrations.AddField(
            model_name='apartment',
            name='area',
            field=models.PositiveIntegerField(default=0, verbose_name='Area (sqft)'),
        ),
        migrations.AddField(
            model_name='commercial',
            name='area',
            field=models.PositiveIntegerField(default=0, verbose_name='Area (sqft)'),
        ),
        migrations.AddField(
            model_name='house',
            name='area',
            field=models.PositiveIntegerField(default=0, verbose_name='Area (sqft)'),
        ),
        migrations.AddField(
            model_name='villa',
            name='area',
            field=models.PositiveIntegerField(default=0, verbose_name='Area (sqft)'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commercial',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='land',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='villa',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]