# Generated by Django 3.2.4 on 2021-06-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0004_alter_recipe_last_made_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='quick_and_easy',
            field=models.BooleanField(default=False),
        ),
    ]
