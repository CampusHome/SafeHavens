# Generated by Django 4.1.4 on 2022-12-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agents', '0002_alter_agent_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]