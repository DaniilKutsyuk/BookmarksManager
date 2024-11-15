# Generated by Django 5.1.3 on 2024-11-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
