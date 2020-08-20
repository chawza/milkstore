# Generated by Django 3.0.5 on 2020-08-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('banner', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
