# Generated by Django 2.0.6 on 2018-06-13 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='language',
        ),
    ]