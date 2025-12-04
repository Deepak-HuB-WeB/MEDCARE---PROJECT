from django import forms
from .models import Doctor, Patient, Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization']


class PatientForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 0, 'max': 120})
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select()
    )

    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender']


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        input_formats=['%H:%M']
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time']
