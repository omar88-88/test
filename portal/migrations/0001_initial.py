# Generated by Django 3.0 on 2020-01-09 11:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('tlf', models.IntegerField(default=11)),
                ('e_post', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='publish_img/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publish1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('tlf', models.IntegerField(default=11)),
                ('e_post', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Time_Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_test', models.DateTimeField()),
                ('bydel', multiselectfield.db.fields.MultiSelectField(choices=[('fjell', 'Fjell'), ('sund', 'Sund'), ('oygarden', 'Øygarden')], max_length=19)),
                ('ham', models.CharField(max_length=30)),
            ],
        ),
    ]