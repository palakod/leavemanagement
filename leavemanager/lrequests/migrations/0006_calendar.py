# Generated by Django 2.1 on 2018-09-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrequests', '0005_auto_20180906_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('occasion', models.CharField(max_length=20)),
            ],
        ),
    ]
