# Generated by Django 4.1 on 2022-09-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0009_alter_contactdata_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactdata",
            name="email",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="contactdata",
            name="fname",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="contactdata",
            name="password",
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name="contactdata",
            name="sname",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="contactdata",
            name="username",
            field=models.CharField(max_length=130),
        ),
    ]
