# Generated by Django 5.0.3 on 2024-03-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheBlog', '0004_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
            ],
        ),
    ]
