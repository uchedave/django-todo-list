# Generated by Django 3.1.3 on 2020-11-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='add_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]