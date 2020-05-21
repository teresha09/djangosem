# Generated by Django 3.0.6 on 2020-05-08 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cover',
            field=models.ImageField(null=True, upload_to=user.models.upload_img_file),
        ),
        migrations.AddField(
            model_name='news',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='news',
            name='headline',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='news_text',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newscomment',
            name='comment_text',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newscomment',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='down_votes',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newscomment',
            name='news',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.News'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newscomment',
            name='up_votes',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
