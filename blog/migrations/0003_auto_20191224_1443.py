# Generated by Django 2.2 on 2019-12-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191224_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.TextField(default='none'),
        ),
    ]