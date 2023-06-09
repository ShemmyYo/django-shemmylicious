# Generated by Django 3.2.18 on 2023-03-25 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_recipe_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingridients',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
