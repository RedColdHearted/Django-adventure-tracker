import functools

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, DetailView

from notes.forms import RegisterForm
from users.models import User

from .models import Note
from .forms import NoteForm

def redirect_to_home_view(request):
    return redirect('notes:home')

def home_page_view(request):
    return render(request, 'notes/home_page.html')

def register_page_view(request):
    return render(request, 'registration/register.html')

@login_required
def profile_page_view(request):
    return render(request, 'notes/profile_page.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Укажите имя вашего шаблона
    redirect_authenticated_user = True
    def get_success_url(self):
        user = self.request.user
        print(user.pk)
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
    template_name = 'notes/profile_page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['notes'] = Note.objects.filter(user=user)
        return context

#note page views
class NoteCreateView(FormView):
    template_name = 'notes/create_form.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes:profile')  # Перенаправление после успешного создания записи

    def form_valid(self, form):
        note = form.save(commit=False)
        note.user = self.request.user
        note.save()
        return super().form_valid(form)

class NoteUpdateView(FormView):
    template_name = 'notes/edit_form.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes:profile')  # Перенаправление после успешного обновления записи

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(instance=get_object_or_404(Note, id=self.kwargs['pk']))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = get_object_or_404(Note, id=self.kwargs['pk'])
        return context