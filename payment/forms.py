from .models import ShoppingAddress
from django import forms


class ShoppingForm(forms.ModelForm):
    shopping_full_name = forms.CharField(label='نام و نام خانوادگی', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی خود را وارد کنید'})
                                         , required=True)

    shopping_email = forms.EmailField(label='ایمیل', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
                                      , required=False)

    shopping_phone_number = forms.CharField(label='شماره تلفن', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شماره تلفن خود را وارد کنید'})
                                            , required=True)
    shopping_address = forms.CharField(label='ادرس1', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ادرس خود را وارد کنید'})
                                       , required=True)

    shopping_city = forms.CharField(label='شهر', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شهر خود را وارد کنید'})
                                    , required=True)
    shopping_state = forms.CharField(label='منطقه', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'منطقه خود را وارد کنید'})
                                     , required=True)
    shopping_zip_code = forms.CharField(label='کدپستی', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'کدپستی خود را وارد کنید'})
                                       , required=False)
    shopping_country = forms.CharField(label='کشور', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'کشور خود را وارد کنید'})
                                       , required=False)

    class Meta:
        model = ShoppingAddress

        fields = ['shopping_full_name', 'shopping_email', 'shopping_phone_number', 'shopping_address', 'shopping_city',
                  'shopping_state', 'shopping_zip_code', 'shopping_country']
