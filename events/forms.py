from django import forms
from .models import Event
from .models import Category
from .models import Registration


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class EventForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, label="Категория")
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'category', 'tags', 'is_visible']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'middle_name', 'birth_date', 'phone_number', 'email']

    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    middle_name = forms.CharField(label='Отчество', max_length=100, required=False)
    birth_date = forms.DateTimeField(label='Дата рождения', widget=forms.DateTimeInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(label='Номер телефона', max_length=15)
    email = forms.EmailField(label='Электронная почта')
