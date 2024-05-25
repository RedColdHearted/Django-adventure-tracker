from django.urls import path
from .views import (
    home_page_view,
    redirect_to_home_view,
    RegisterView,
    NoteCreateView, NoteUpdateView, UserProfileView, CustomLoginView, delete_note_view
)

app_name = 'notes'

urlpatterns = [
    path('', redirect_to_home_view, name='redirect_to_home'),
    path('home/', home_page_view, name='home'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/create-note/', NoteCreateView.as_view(), name='create-note'),
    path('profile/update-note/<uuid:uuid>', NoteUpdateView.as_view(), name='update-note'),
    path('profile/delete-note/<uuid:uuid>/', delete_note_view, name='delete-note'),
]