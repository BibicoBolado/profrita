# Generated by Django 2.0.1 on 2018-05-04 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]