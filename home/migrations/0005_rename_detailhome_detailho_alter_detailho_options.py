# Generated by Django 4.1.1 on 2023-05-11 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_detailho_detailhome'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Detailhome',
            new_name='detailho',
        ),
        migrations.AlterModelOptions(
            name='detailho',
            options={},
        ),
    ]
