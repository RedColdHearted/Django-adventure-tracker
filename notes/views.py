from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, DetailView, UpdateView

from notes.forms import RegisterForm
from users.models import User

from .models import Note
from .forms import NoteCreateForm, NoteUpdtateForm

def redirect_to_home_view(request):
    return redirect('notes:home')

def home_page_view(request):
    return render(request, 'notes/home_page.html')

def register_page_view(request):
    return render(request, 'registration/register.html')

@login_required
def profile_page_view(request):
    return render(request, 'notes/profile/profile_page.html')

@login_required
def delete_note_view(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.user.id != note.user_id:
        return HttpResponseForbidden("У вас нет разрешения на удаление этой заметки.")

    note.delete()
    return redirect('notes:login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        user = self.request.user
        return reverse('notes:profile', kwargs={'pk': user.pk})

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('notes:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.profile_image = self.request.FILES.get('profile_image')
        user.save()
        return super().form_valid(form)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'notes/profile/profile_page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['notes'] = Note.objects.filter(user=user)
        for i in range(len(context['notes'])):
            x, y = context['notes'][i].location.split(',')
            x, y = float(x.lstrip('[')), float(y.rstrip(']'))
            context['notes'][i].x = x
            context['notes'][i].y = y
            context['notes'][i].hash = hash((x, y)) % 1000
        return context

#note page views
class NoteCreateView(FormView):
    template_name = 'notes/forms/create_form.html'
    form_class = NoteCreateForm
    success_url = reverse_lazy('notes:login')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.user = self.request.user
        note.save()
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteUpdtateForm
    template_name = 'notes/forms/edit_form.html'
    success_url = reverse_lazy('notes:login')
    pk_url_kwarg = 'uuid'

    def get_queryset(self):
        """
        Ограничение прав доступа к редактированию заметки только её создателю.
        """
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
