from django import forms
from .models import Students

class AddStudenttForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'dob', 'gender', 'address', 'phone_no', 'standard', 'age']
        
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=Students.gender_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    standard = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Standard'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}))
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass