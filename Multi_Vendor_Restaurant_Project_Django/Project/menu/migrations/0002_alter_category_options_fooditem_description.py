# Generated by Django 4.1.3 on 2022-12-14 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='fooditem',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
