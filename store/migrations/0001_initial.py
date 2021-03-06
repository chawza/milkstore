# Generated by Django 3.0.5 on 2020-08-19 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment', models.CharField(default='DEBIT', max_length=255)),
                ('customer_address', models.CharField(default='', max_length=255)),
                ('items', models.TextField(default='')),
                ('store_address', models.CharField(default='', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.Store')),
            ],
        ),
    ]
