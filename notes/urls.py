from django.urls import path
from .views import profile_page_view, home_page_view, redirect_to_home_view, login_page_view, RegisterView

app_name = 'notes'

urlpatterns = [
    path('', redirect_to_home_view, name='redirect_to_home'),
    path('home/', home_page_view, name='home'),
    path('profile/', profile_page_view, name='profile'),
    path('login/', login_page_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]