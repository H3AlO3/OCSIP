# Generated by Django 4.1 on 2023-12-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_rename_token_data_password_md5"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="password_md5",
            field=models.CharField(max_length=50, verbose_name="密码(md5))"),
        ),
    ]
