# Generated by Django 4.2.1 on 2023-05-14 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AirCraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('AN158', 'An158'), ('Boeing747', 'Boeing747'), ('DouglasDC3', 'Douglasdc3'), ('AirbusA380', 'Airbusa380'), ('Boeing777X', 'Boeing777X')], default='AN158', max_length=12)),
                ('capacity', models.IntegerField()),
                ('payload', models.IntegerField()),
                ('flight_distance', models.IntegerField()),
                ('fuel_per_hour', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aircrafts', to='main.airline')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
