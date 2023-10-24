# Generated by Django 4.2.6 on 2023-10-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_popular_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popular_items',
            name='coffee',
        ),
        migrations.AddField(
            model_name='popular_items',
            name='coffee',
            field=models.ManyToManyField(to='main.coffee'),
        ),
    ]