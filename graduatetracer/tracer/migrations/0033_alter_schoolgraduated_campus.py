# Generated by Django 4.0.5 on 2022-09-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0032_schoolgraduated_user_argao_campus_user_barili_campus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolgraduated',
            name='campus',
            field=models.CharField(blank=True, choices=[('Argao Campus', 'Argao Campus'), ('Barili Campus', 'Barili Campus'), ('Carmen Campus', 'Carmen Campus'), ('Cebu City Mountain Extension Campus', 'Cebu City Mountain Extension Campus'), ('Daanbantayan Campus', 'Daanbantayan Campus'), ('Danao Campus', 'Danao Campus'), ('Dumanjug Extension Campus', 'Dumanjug Extension Campus'), ('Ginatilan Extension Campus', 'Ginatilan Extension Campus'), ('Main Campus', 'Main Campus'), ('Moalboal Campus', 'Moalboal Campus'), ('Naga Extension Campus', 'Naga Extension Campus'), ('Oslob Extension Campus', 'Oslob Extension Campus'), ('Pinamungajan Extension Campus', 'Pinamungajan Extension Campus'), ('San Fernando Extension Campus', 'San Fernando Extension Campus'), ('San Francisco Campus', 'San Francisco Campus'), ('Tuburan Campus', 'Tuburan Campus')], max_length=100, null=True),
        ),
    ]