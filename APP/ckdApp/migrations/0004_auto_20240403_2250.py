# Generated by Django 3.0.2 on 2024-04-03 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckdApp', '0003_auto_20240307_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='compactness_worst',
            new_name='Acid_Level_Check_Normal_input',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='concavity_mean',
            new_name='Maintenance_History_Neglected_input',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='concavity_worst',
            new_name='Maintenance_History_No_maintenance_input',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='radius_mean',
            new_name='Maintenance_History_Regular_maintenance_input',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='radius_worst',
            new_name='Open_Circuit_Voltage_input',
        ),
    ]
