from django import forms

from django.forms import ModelForm

from .models import *

GENDER_CHOICES = (
    (None, '-None-'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender')
)



class DriverForm(ModelForm):
    class Meta:
        model = DriverModel
        exclude = ['created_dtm', 'updated_dtm']

    # name = forms.CharField(label='Name', max_length=45, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control', 'id': 'txtFirstName', 'autocomplete': False, 'required': True,
    #         'placeholder': ''
    #     }))
    # gender = forms.CharField(label='Suffix', max_length=5, required=False, widget=forms.Select(choices=GENDER_CHOICES,
    #                                                                                            attrs={
    #                                                                                                'class': 'form-control',
    #                                                                                                'id': 'GENDER',
    #                                                                                                'autocomplete': False
    #
    #                                                                                            }))
    # address = forms.CharField(label='Address Line', max_length=150, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control no-upscope', 'id': 'txtStreetAddress', 'autocomplete': False,
    #         'required': True
    #     }))
    # city = forms.CharField(label='City', max_length=30, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control no-upscope', 'id': 'txtCity', 'autocomplete': False, 'required': True,
    #     }))
    # state = forms.CharField(label='State', max_length=150, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control no-upscope', 'id': 'txtState', 'autocomplete': False,
    #         'required': True
    #     }))
    # pincode = forms.CharField(label='Pin Code', max_length=10, widget=forms.TextInput(
    #     attrs={'class': 'form-control no-upscope', 'id': 'txtPin', 'autocomplete': False, 'required':
    #         True}))

    def clean(self):
        return self.cleaned_data


class ConsigneeForm(ModelForm):
    class Meta:
        model = ConsigneeModel
        exclude = ['created_dtm', 'updated_dtm']

    def clean(self):
        return self.cleaned_data


class ConsignorForm(ModelForm):
    class Meta:
        model = ConsignorModel
        exclude = ['created_dtm', 'updated_dtm']

    def clean(self):
        return self.cleaned_data


class ShippingOrdersForm(ModelForm):
    class Meta:
        model = ShippingOrdersModel
        exclude = ['created_dtm', 'updated_dtm']
        widgets = {
            'freight_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'lr_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'hamali_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'door_collection': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'door_delivery': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'other_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control charges'
                }
            ),
            'total_charges': forms.NumberInput(
                attrs={
                    'class': 'form-control total-charges'
                }
            )
        }
    def clean(self):
        return self.cleaned_data
