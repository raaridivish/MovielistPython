# Generated by Django 4.0.3 on 2022-04-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dffff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
