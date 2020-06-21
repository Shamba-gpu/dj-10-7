from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

from .forms import SignupForm, LoginForm


def home(request):
    return render(request, 'home.html')

class Login_View(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

class Logout_View(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = '/'

    def form_valid(self, form):
        formvalid = super(SignupView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        # messages.success(request, 'Вы зарегистрировались!')
        login(self.request, user)
        return formvalid

