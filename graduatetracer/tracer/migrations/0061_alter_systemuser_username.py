# Generated by Django 4.1.1 on 2022-09-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0060_alter_systemuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='username',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
