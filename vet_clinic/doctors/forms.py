from django import forms

from vet_clinic.pet_patients.models import Treatment


class AssignTreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['date', 'diagnose', 'treatment_type', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(AssignTreatmentForm, self).__init__(*args, **kwargs)
