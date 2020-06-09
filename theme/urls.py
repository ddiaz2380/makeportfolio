from django.urls import path

from .views import DefaultThemeView
from .views import theme_preview, theme_setup, profile_setting

urlpatterns = [
    path('', DefaultThemeView.as_view(), name='default-theme'),
    path('preview/<theme_id>', theme_preview, name='theme-preview'),
    path('theme-setup/<theme_id>/', theme_setup, name='theme-setup'),
    path('profile/<int:user_id>/settings/', profile_setting, name='profile-setting'),
]