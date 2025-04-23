from django import forms
from .models import medicines, health


class healthForm(forms.ModelForm):
    class Meta:
        model = health
        fields = '__all__'
        labels = {
            'hname' : 'health Name ',
            'hprice' : 'Price',
            'hinfo' : "health Info",
            'himg': 'health Image'
        }
        widget = {
            'hname' : forms.TextInput(attrs={'class': 'form-control'}),
            'hprice' : forms.NumberInput(attrs={'class': 'form-control'}),
            'himg' : forms.FileInput(attrs={'class': 'form-control'}),
            'hinfo' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class medicinesForm(forms.ModelForm):
    class Meta:
        model = medicines
        fields = '__all__'
        labels = {
            'mname' : 'medicines Name ',
            'mprice' : 'Price',
            'minfo' : "medicines Info",
            'mimg': 'medicines Image'
        }
        widget = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'mprice' : forms.NumberInput(attrs={'class': 'form-control'}),
            'mimg' : forms.FileInput(attrs={'class': 'form-control'}),
            'minfo' : forms.Textarea(attrs={'class': 'form-control'}),
        }
