# Generated by Django 3.0.2 on 2024-03-07 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckdApp', '0002_auto_20200205_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='Blood_Urea',
            new_name='compactness_worst',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='Blood_Glucose_Random',
            new_name='concavity_mean',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='Packed_cell_volume',
            new_name='concavity_worst',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='Serum_Creatine',
            new_name='radius_mean',
        ),
        migrations.RenameField(
            model_name='ckdmodel',
            old_name='White_blood_count',
            new_name='radius_worst',
        ),
    ]
