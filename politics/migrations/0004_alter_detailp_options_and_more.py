# Generated by Django 4.1.1 on 2023-05-05 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0003_rename_detail_detailp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailp',
            options={},
        ),
        migrations.RenameField(
            model_name='detailp',
            old_name='content',
            new_name='contents',
        ),
    ]
