# Generated by Django 4.2.6 on 2023-10-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_coffee_category_coffee_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Text Name')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Textes',
            },
        ),
        migrations.RemoveField(
            model_name='daily_menu',
            name='about1',
        ),
        migrations.RemoveField(
            model_name='daily_menu',
            name='about2',
        ),
        migrations.RemoveField(
            model_name='daily_menu',
            name='about3',
        ),
        migrations.RemoveField(
            model_name='daily_menu',
            name='about4',
        ),
        migrations.RemoveField(
            model_name='daily_menu',
            name='about5',
        ),
        migrations.RemoveField(
            model_name='daily_menu',
            name='about6',
        ),
        migrations.AddField(
            model_name='daily_menu',
            name='about',
            field=models.ManyToManyField(to='main.text'),
        ),
    ]
