from .models import User
from django.forms import ModelForm, TextInput

class RegForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'email', 'name', 'surname', 'psw_hash', 'phone']

        widgets = {
            'login': TextInput(attrs={
                'placeholder': 'Логин'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Почта'
            }),
            'name': TextInput(attrs={
                'placeholder': 'Имя'
            }),
            'surname': TextInput(attrs={
                'placeholder': 'Фамилия'
            }),
            'psw_hash': TextInput(attrs={
                'placeholder': 'Пароль'
            }),
            'phone': TextInput(attrs={
                'placeholder': 'Телефон'
            })
        }

class LogForm():
    pass