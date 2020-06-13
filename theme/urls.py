from django.urls import path

from .views import DefaultThemeView, ThemeList
from .views import theme_preview, theme_setup

urlpatterns = [
    path('', DefaultThemeView.as_view(), name='default-theme'),
    path('list/', ThemeList.as_view(), name='theme-list'),
    path('preview/<theme_id>', theme_preview, name='theme-preview'),
    path('theme-setup/<theme_id>/', theme_setup, name='theme-setup'),
]