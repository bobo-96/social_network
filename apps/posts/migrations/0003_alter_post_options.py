# Generated by Django 4.0 on 2021-12-16 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
