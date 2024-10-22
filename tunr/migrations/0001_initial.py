# Generated by Django 5.0.7 on 2024-07-15 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hours', models.CharField()),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to='tunr.city')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tunr.attraction')),
            ],
        ),
    ]
