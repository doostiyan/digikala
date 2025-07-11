import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from payment.models import ShoppingAddress
from accounts.forms import UserCreationForm, UserLoginForm, UpdateProfileForm, UpdatePasswordForm, UpdateUserInfoForm
from accounts.models import Profile
from orders.cart import Cart
from payment.forms import ShoppingForm

class RegisterUserView(View):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shop:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'با موفقیت ثبت نام کردید', 'success')
            return redirect('shop:home')
        return render(request, self.template_name, {'form': form})


class LoginUserView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('shop:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                current_user = Profile.objects.get(user__id=request.user.id)
                saved_cart = current_user.old_cart

                if saved_cart:
                    converted_cart = json.loads(saved_cart)
                    cart = Cart(request)
                    for key, value in converted_cart.items():
                        cart.db_add(product=key, quantity=value)

                messages.success(request, 'با موفقیت وارد شدید', 'success')
                return redirect('shop:home')
            messages.error(request, 'اطلاعات نامعتبر است', 'danger')
            return render(request, self.template_name, {'form': form})


class LogoutUserView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت خارج شدید!', 'info')
        return redirect('shop:home')

class UpdateUserView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        form = UpdateProfileForm(instance=user)
        return render(request, 'accounts/update_user.html' , {'form': form})

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        form = UpdateProfileForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            messages.success(request, 'پروفایل شما ویرایش شد ')
            return redirect('shop:home')
        return render(request, 'accounts/update_user.html', {'form': form})


def update_password(request):
    if request.user.is_authenticated:
        user_new = request.user
        if request.method == 'POST':
            form = UpdatePasswordForm(user_new, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'رمز با موفقیت ویرایش شد')
                return redirect('accounts:login')
            else:
                for err in list(form.errors.values()):
                    messages.warning(request, err)
                return redirect('accounts:update_password')
        else:
            form = UpdatePasswordForm(user_new)
            return render(request, 'accounts/update_password.html', {"form": form})
    else:
        messages.error(request, 'ابتدا باید لاگین کنی')
        return redirect('accounts:login')


def update_info(request):
    if request.user.is_authenticated:
        try:
            new_user = Profile.objects.get(user=request.user)
            shopping_user = ShoppingAddress.objects.get(user=request.user)
        except (Profile.DoesNotExist, ShoppingAddress.DoesNotExist):
            messages.error(request, 'پروفایل یا آدرس شما یافت نشد. لطفاً با پشتیبانی تماس بگیرید.')
            return redirect('shop:home')

        if request.method == 'POST':
            form = UpdateUserInfoForm(request.POST, instance=new_user)
            shopping_form = ShoppingForm(request.POST, instance=shopping_user)
            if form.is_valid() and shopping_form.is_valid():
                form.save()
                shopping_form.save()
                messages.success(request, 'اطلاعات شما با موفقیت به‌روزرسانی شد.')
                return redirect('shop:home')
        else:
            form = UpdateUserInfoForm(instance=new_user)
            shopping_form = ShoppingForm(instance=shopping_user)

        context = {
            'form': form,
            'shopping_form': shopping_form
        }
        return render(request, 'accounts/update_info.html', context)
    else:
        messages.error(request, 'ابتدا باید وارد حساب کاربری خود شوید.')
        return redirect('accounts:login')