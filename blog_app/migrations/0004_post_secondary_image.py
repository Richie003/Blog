# Generated by Django 4.0 on 2024-01-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='secondary_image',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
