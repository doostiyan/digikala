from django.urls import path

from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('update_user/', views.UpdateUserView.as_view(), name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
]