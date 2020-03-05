from django import forms

from .models import MedicalInfo

class AddMedicalInfoForm(forms.ModelForm):

    class Meta:
        fields = ("blood_group", "diagnosis", "vital_signs", "medications", "allergies")
        model = MedicalInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['diagnosis'].help_text = 'Note that your personality will not be associated publically with the diagnosis.'
        self.fields['vital_signs'].help_text = "Please, enter your vital signs if more than one, seperate by commas."
        self.fields['vital_signs'].label = "Vital signs"

        self.fields['medications'].help_text = "Please, enter your medications if more than one, seperate by commas."
        self.fields['medications'].label = "Medications"

        self.fields['allergies'].help_text = "Please, enter your allergies if more than one, seperate by commas (optional)."
        self.fields['allergies'].label = "Allergies (optional)"