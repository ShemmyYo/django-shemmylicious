# Generated by Django 3.2.18 on 2023-04-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]