# Generated by Django 2.0.1 on 2020-10-12 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20201012_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='topic',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='topic',
            new_name='name',
        ),
    ]
