# Generated by Django 5.0.3 on 2024-03-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheBlog', '0008_post_snippets'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
