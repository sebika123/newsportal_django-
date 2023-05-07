# Generated by Django 4.1.1 on 2023-05-06 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('content', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sports.content')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='sports.content')),
            ],
        ),
    ]
