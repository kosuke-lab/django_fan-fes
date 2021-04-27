# Generated by Django 3.1.4 on 2021-04-24 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('festival', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=400, verbose_name='コメント欄'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='start_time',
            field=models.CharField(max_length=200, null=True, verbose_name='開催日'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='thumbnail',
            field=models.ImageField(default='img/no_image.jpeg', upload_to='img/', verbose_name='サムネイル'),
        ),
    ]