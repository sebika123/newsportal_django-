# Generated by Django 4.1.1 on 2023-04-22 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='detailh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('content', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='health.content')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='health.content')),
            ],
        ),
    ]
