# Generated by Django 3.2.4 on 2021-06-27 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0005_alter_recipe_quick_and_easy'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='saved_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='saved_recipes', to='recipe_app.user'),
        ),
    ]
