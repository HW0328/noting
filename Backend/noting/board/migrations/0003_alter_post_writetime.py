# Generated by Django 5.0.1 on 2024-04-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_writetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writetime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
