from django.urls import path
from .views import (  # profile_page_view,
    home_page_view,
    redirect_to_home_view,
    # login_page_view,
    RegisterView,
    NoteCreateView,
    NoteUpdateView, UserProfileView, CustomLoginView
)

app_name = 'notes'

urlpatterns = [
    path('', redirect_to_home_view, name='redirect_to_home'),
    path('home/', home_page_view, name='home'),
    # path('profile/', profile_page_view, name='profile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    # path('login/', login_page_view, name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('create-note/<str:pk>', NoteCreateView.as_view(), name='create-note'),
    path('create-note/<str:pk>', NoteUpdateView.as_view(), name='update-note')
]