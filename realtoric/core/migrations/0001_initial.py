# Generated by Django 3.2.15 on 2022-09-10 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=512)),
                ('type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Villa', 'Villa'), ('Commercial', 'Commercial'), ('Land', 'Land')], default='House', max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('google_maps', models.URLField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to='properties')),
                ('sale_status', models.CharField(choices=[('For Sale', 'For Sale'), ('Sold', 'Sold')], default='For Sale', max_length=50)),
                ('contact_info', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]