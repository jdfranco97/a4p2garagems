from django.urls import path
from .views import SignUpView
from django.contrib.auth import views



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
