from .models import ShopingAddress
from django import forms
class ShopingForm(forms.ModelForm):
    shoping_full_name = forms.CharField(label='نام و نام خانوادگی', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی خود را وارد کنید'})
        , required=True)
    
    shoping_email = forms.EmailField(label='ایمیل', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
                            , required=False)

    shoping_phone_number = forms.CharField(label='شماره تلفن', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شماره تلفن خود را وارد کنید'})
                            , required=True)
    shoping_address = forms.CharField(label='ادرس1', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ادرس خود را وارد کنید'})
                            , required=True)

    shoping_city = forms.CharField(label='شهر', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شهر خود را وارد کنید'})
                            , required=True)
    shoping_state = forms.CharField(label='منطقه', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'منطقه خود را وارد کنید'})
                            , required=True)
    shoping_zipcode = forms.CharField(label='کدپستی', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'کدپستی خود را وارد کنید'})
                            , required=False)
    shoping_country = forms.CharField(label='کشور', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'کشور خود را وارد کنید'})
                            , required=False)
    
    class Meta:
        model = ShopingAddress

        fields = ['shoping_full_name', 'shoping_email', 'shoping_phone_number', 'shoping_address', 'shoping_city', 'shoping_state', 'shoping_zipcode', 'shoping_country']

