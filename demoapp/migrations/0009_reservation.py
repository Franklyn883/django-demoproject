# Generated by Django 4.1 on 2023-05-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_logger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200, verbose_name='Phone Number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
