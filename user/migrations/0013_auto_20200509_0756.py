# Generated by Django 3.0.6 on 2020-05-09 07:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200509_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.UUIDField(default=uuid.UUID('bc620933-7455-4413-8be2-d1c463a8fb4f'), editable=False),
        ),
    ]
