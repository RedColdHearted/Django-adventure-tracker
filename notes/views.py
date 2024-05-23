import functools

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from notes.forms import RegisterForm
from users.models import User


def register_redirect(func):
    @functools.wraps(func)
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('notes:profile')
        value = func(request)
        return value
    return wrapper

@register_redirect
def redirect_to_home_view(request):
    return redirect('notes:home')

@register_redirect
def home_page_view(request):
    return render(request, 'notes/home_page.html')

@register_redirect
def login_page_view(request):
    return render(request, 'registration/login.html')

def register_page_view(request):
    return render(request, 'registration/register.html')

@login_required
def profile_page_view(request):
    return render(request, 'notes/profile_page.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('notes:profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.profile_image = self.request.FILES.get('profile_image')
        user.save()
        return super().form_valid(form)