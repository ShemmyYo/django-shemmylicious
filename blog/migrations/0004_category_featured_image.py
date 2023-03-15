# Generated by Django 3.2.18 on 2023-03-15 15:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_recipe_featured_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='featured-recipe', max_length=255, verbose_name='image'),
        ),
    ]