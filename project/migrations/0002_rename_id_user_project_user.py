# Generated by Django 5.0.2 on 2024-02-26 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='id_user',
            new_name='user',
        ),
    ]