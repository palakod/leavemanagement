# Generated by Django 2.1 on 2018-09-04 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lrequests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='employee_ID',
        ),
    ]
