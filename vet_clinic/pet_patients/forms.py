from django import forms

from vet_clinic.pet_patients.models import PetPatient


class PetPatientBaseForm(forms.ModelForm):
    class Meta:
        model = PetPatient
        fields = ('name', 'species', 'breed', 'weight', 'gender', 'color', 'date_of_birth', 'notes')
        labels = {
            'name': 'Pet name:',
            'date_of_birth': 'Date of birth:',
            'species': 'Species:',
            'breed': 'Breed:',
            'weight': 'Weight (kg):',
            'gender': 'Gender:',
            'color': 'Color:',
            'notes': 'Notes:',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'placeholder': 'Breed'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Weight'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'placeholder': 'Color'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes', 'rows': 4}),
        }


class PetPatientCreateForm(PetPatientBaseForm):
    pass


class PetPatientEditForm(PetPatientBaseForm):
    pass
