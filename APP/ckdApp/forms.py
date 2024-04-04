from django import forms
from .models import *



class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['Open_Circuit_Voltage_input','Maintenance_History_Neglected_input','Maintenance_History_No_maintenance_input','Maintenance_History_Regular_maintenance_input','Acid_Level_Check_Normal_input']
