# Generated by Django 3.2.7 on 2021-12-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0007_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='workExperiences',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
