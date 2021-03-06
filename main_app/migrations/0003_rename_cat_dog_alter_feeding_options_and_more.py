# Generated by Django 4.0.5 on 2022-07-08 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='Dog',
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='feeding',
            old_name='cat',
            new_name='dog',
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
    ]
