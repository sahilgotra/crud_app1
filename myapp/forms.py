from django import forms

from .models import registration
GENDER_CHOICES = (
  ('male', 'male'),
  ('female', 'female')
)

JOB_CHOICES=(
  ('chandigarh', 'chandigarh'),
  ('mohali', 'mohali'),
  ('pune', 'pune'),
  ('mumbai', 'mumbai')
)
STATE_CHOICE = (
  ('jammu and kashmir', 'J&K'),
  ('Haryana', 'Haryana'),
  ('Punjab', 'Punjab'),
  ('Himachal Pradesh', 'Himachal Pradesh')
)
class regForm(forms.ModelForm):
  gender = forms.ChoiceField(choices=GENDER_CHOICES,  widget=forms.RadioSelect)
  job_location = forms.MultipleChoiceField(choices=JOB_CHOICES, widget = forms.CheckboxSelectMultiple)
  state = forms.ChoiceField(choices=STATE_CHOICE)
  class Meta:
    model = registration
    fields = ['name', 'dob', 'gender', 'state', 'city', 'pin', 'mobile', 'email', 'job_location', 'image', 'file']

    widgets= {
      'name':forms.TextInput(attrs={'class':'form-control', 'id':'form-control'}),
      'dob': forms.DateInput(attrs={'id':'datepicker', 'class':'form-control'}),
      # 'state': forms.Select(attrs={'id':'datepicker', 'class':'form-control'}),
      'city': forms.DateInput(attrs={'id':'city', 'class':'form-control'}),
      'pin': forms.NumberInput(attrs={'id':'pin', 'class':'form-control'}),
      'mobile': forms.NumberInput(attrs={'id':'mobile', 'class':'form-control'}),
      'email': forms.DateInput(attrs={'id':'email', 'class':'form-control'}),
      
      
    }