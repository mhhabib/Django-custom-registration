from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# from .views import MyView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset_passord/', auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"),
         name="reset_password"),
    path('reset_passord_sent/', auth_views.PasswordResetDoneView.as_view(template_name="base/reset_passord_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_passord_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset_done.html"),
         name="password_reset_complete"),
]
