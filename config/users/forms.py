from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):

    height = forms.DecimalField(
        label='Рост',
        max_digits=5, 
        decimal_places=2,
        required=False
    )

    weight = forms.DecimalField(
        label='Вес', 
        max_digits=5,
        decimal_places=2,
        required=False  
    )

    blood_pressure = forms.CharField(
        label='Давление',
        max_length=20,
        required=False
    )

    heart_rate = forms.IntegerField(
        label='Пульс',
        required=False
    )

    date_of_birth = forms.DateField(
        label='Дата рождения',
        required=False
    )
    
    GENDER_CHOICES = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
    ]

    gender = forms.ChoiceField(
        label='Пол',
        choices=GENDER_CHOICES,
        required=False 
    )

    address = forms.CharField(
        label='Адрес', 
        widget=forms.Textarea,
        required=False
    )

    profile_photo = forms.ImageField(
        label='Фото профиля',
        required=False
    )

    class Meta:
        model = UserProfile
        fields = [
            'height', 
            'weight',
            'blood_pressure',
            'heart_rate',
            'date_of_birth',
            'gender',
            'address',
            'profile_photo'
        ]


class UserProfileForm(forms.ModelForm):
    
    class Meta:
         model = UserProfile
         fields = [
            'height', 
            'weight',
            'blood_pressure',
            'heart_rate',
            'date_of_birth',
            'gender',
            'address',
            'profile_photo'
         ]