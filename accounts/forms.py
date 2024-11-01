from django import forms
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import Profile


class UserCreationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('رمز عبور باید یکسان باشد')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل وجود دارد')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('این یوزرنیم وجود دارد')
        return username


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمزعبور خود را وارد کنید'}))


class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام را وارد کنید'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی را وارد کنید'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')


class UpdateUserInfoForm(forms.ModelForm):
    phone = forms.CharField(label='شماره تلفن', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شماره تلفن خود را وارد کنید'})
                            , required=False)
    address1 = forms.CharField(label='ادرس1', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ادرس خود را وارد کنید'})
                            , required=False)
    address2 = forms.CharField(label='ادرس2', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ادرس خود را وارد کنید'})
                            , required=False)
    city = forms.CharField(label='شهر', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شهر خود را وارد کنید'})
                            , required=False)
    state = forms.CharField(label='منطقه', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'منطقه خود را وارد کنید'})
                            , required=False)
    zipcode = forms.CharField(label='کدپستی', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'کدپستی خود را وارد کنید'})
                            , required=False)
    country = forms.CharField(label='کشور', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'کشور خود را وارد کنید'})
                            , required=False)

    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country')
