# Generated by Django 2.2 on 2019-12-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_article_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.TextField(default='none'),
        ),
    ]
