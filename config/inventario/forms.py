from django.forms import ModelForm, TextInput
from .models import *

class EntradasInvForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cantidad'].widget.attrs['autofocus'] = True

    class Meta:
        model = EntradaInventario
        fields = '__all__'
        widgets = {
            'cantidad': TextInput(
                attrs={
                    'placeholder': '#',
                }
            )
        }


class SalidasInvForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cantidad'].widget.attrs['autofocus'] = True

    class Meta:
        model = SalidaInventario
        fields = '__all__'
        widgets = {
            'cantidad': TextInput(
                attrs={
                    'placeholder': '#',
                }
            )
        }