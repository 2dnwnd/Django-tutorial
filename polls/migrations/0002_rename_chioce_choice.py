# Generated by Django 4.0.3 on 2022-03-08 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chioce',
            new_name='Choice',
        ),
    ]
