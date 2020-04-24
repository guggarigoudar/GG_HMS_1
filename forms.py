from django import forms
import datetime
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import IpdRegister
from .models import OpdRegister
from .models import Seeds


class frmOpdRegister(forms.ModelForm):
    # my_default_errors = {
    #   'required': 'HELLO DADDY',
    #  'invalid': 'WORLD'
    # }

    pin = forms.CharField(max_length=6, min_length=6, required=True, validators=[RegexValidator(regex='\d{6}')],
                          error_messages=({'invalid': 'has to be a 6 digit number'}))  # ? overldes model field
    mobile = forms.CharField(max_length=10, min_length=10, required=True, validators=[RegexValidator(regex='\d{10}')],
                             error_messages=({'invalid': 'has to be a 10 digit number'}))  # ? overides model field
    age = forms.CharField(max_length=2, min_length=1, required=True,
                          validators=[RegexValidator(regex='^[1-9]$|^[1-9][0-9]$')],
                          error_messages=({'invalid': 'has to be a  1 or 2 digit number'}))  # ? overides model field
    doa = forms.CharField(initial=datetime.date.today, disabled=True)

    # first_name=forms.CharField(min_length='2',error_messages={'blank':'Guggarigoudar'})

    class Meta:
        model = OpdRegister
        #    fields = "__all__"
        fields = ['age', 'pin', 'mobile', 'opno', 'photo']


class frmIpdRegister(forms.ModelForm):
    class Meta:
        model = IpdRegister
        fields = "__all__"
        exclude = ['age_in_days', 'mother', 'father', 'husband', 'user', ]


class seedsData(forms.ModelForm):
    class Meta:
        model = Seeds
        fields = ['prefix', ]
        labels = {'prefix': 'OP No'}  # customise label
