from django.forms import ModelForm, TextInput
from django import forms
from .models import *


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cli'].widget.attrs['autofocus'] = True

        self.fields['subtotal'].widget.attrs= {
            'readonly':True,
            'class': 'form-control',
        }

        self.fields['total'].widget.attrs= {
            'readonly':True,
            'class': 'form-control',
        }

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': forms.Select(attrs={'class': 'form-control'}),
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese un producto',
                }
            )
        }


class pedidoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cantidad'].widget.attrs['autofocus'] = True

        # self.fields['subtotal'].widget.attrs= {
        #     'readonly':True,
        #     'class': 'form-control',
        # }

        # self.fields['total'].widget.attrs= {
        #     'readonly':True,
        #     'class': 'form-control',
        # }

    class Meta:
        model = pedido
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': TextInput(
                attrs={
                    'placeholder': 'Ingrese una cantidad',
                }
            )
        }


class MesaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cli'].widget.attrs['autofocus'] = True

        # self.fields['total'].widget.attrs= {
        #     'readonly':True,
        #     'class': 'form-control',
        # }

    class Meta:
        model = Mesa
        fields = '__all__'
        widgets = {
            'cli': forms.Select(attrs={'class': 'form-control'}),
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese una mesa',
                }
            )
        }