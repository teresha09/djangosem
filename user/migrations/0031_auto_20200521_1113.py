# Generated by Django 3.0.6 on 2020-05-21 11:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_auto_20200521_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.UUIDField(default=uuid.UUID('cce18f3d-e344-4475-ba3b-9232c54b411a'), editable=False),
        ),
    ]
