# Generated by Django 4.2.1 on 2023-07-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='News_title',
            field=models.CharField(default='news title', max_length=100),
        ),
    ]
