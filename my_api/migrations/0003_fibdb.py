# Generated by Django 3.1.4 on 2020-12-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0002_auto_20201211_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='FibDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
    ]