# Generated by Django 4.1.1 on 2023-05-04 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('image', models.ImageField(upload_to='home')),
            ],
            options={
                'verbose_name': 'home',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('content', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.content')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='home.content')),
            ],
            options={
                'verbose_name': 'details',
            },
        ),
    ]