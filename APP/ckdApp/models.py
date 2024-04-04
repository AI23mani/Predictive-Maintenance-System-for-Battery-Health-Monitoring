from django.db import models

class ckdModel(models.Model):
    Open_Circuit_Voltage_input = models.FloatField()
    Maintenance_History_Neglected_input = models.FloatField()
    Maintenance_History_No_maintenance_input = models.FloatField()
    Maintenance_History_Regular_maintenance_input = models.FloatField()
    Acid_Level_Check_Normal_input = models.FloatField()

    def __str__(self):
        return str(self.pk)
