# Generated by Django 3.0.6 on 2020-05-13 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20200513_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.UUIDField(default=uuid.UUID('cf82a092-7bc8-44d5-a040-20b9541d10a3'), editable=False),
        ),
    ]
