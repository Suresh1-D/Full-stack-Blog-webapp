# Generated by Django 5.1.6 on 2025-02-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]
