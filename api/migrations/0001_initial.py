# Generated by Django 3.1.7 on 2021-03-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(default='Cuisine', max_length=20)),
                ('serving_size', models.SmallIntegerField(default=1)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Kona', max_length=20)),
                ('last_name', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
