# Generated by Django 4.0.1 on 2022-02-07 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False),
        ),
    ]
