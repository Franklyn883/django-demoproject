# Generated by Django 4.2.1 on 2023-05-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0009_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='cuisine',
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]