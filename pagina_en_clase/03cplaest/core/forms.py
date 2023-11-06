


from django import forms
from .models import GrantGoal

class GrantGoalForm(forms.ModelForm):
    class Meta:
        model = GrantGoal
        fields = "__all__"
        exclude = ["timestamp", "final_date"]
        widgets = {
            "user": forms.Select(attrs={"type":"select","class":"form-select"}),
            "gg_title": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre del GrantGoal"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe la descripcion del GrantGoal"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox", "class":"form-checkbox"}),
            "state": forms.Select(attrs={"type":"select","class":"form-select"}),
            "sprint":forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "slug":forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el codigo del GrantGoal"}),
        }



class UpdateGrantGoalForm(forms.ModelForm):
    class Meta:
        model = GrantGoal
        fields = "__all__"
        exclude = ["timestamp", "final_date"]
        widgets = {
            "user": forms.Select(attrs={"type":"select","class":"form-select"}),
            "gg_title": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre del GrantGoal"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe la descripcion del GrantGoal"}),
            "days_duration": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox", "class":"form-checkbox"}),
            "state": forms.Select(attrs={"type":"select","class":"form-select"}),
            "sprint":forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
            "slug":forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el codigo del GrantGoal"}),
        }