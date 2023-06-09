# Generated by Django 4.1.1 on 2023-04-29 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('politics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'politics'},
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('content', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='politics.content')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='politics.content')),
            ],
            options={
                'verbose_name': 'detailsp',
            },
        ),
    ]
