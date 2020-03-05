from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, View
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import UserSignUpForm, UserSignInForm

# Create your views here.
class SignUp(CreateView):
  form_class = UserSignUpForm
  success_url = reverse_lazy('signin')
  template_name = 'users/signup.html'


class SignInView(View):
  def get(self, request):
    form = UserSignInForm()
    return render(request, 'users/signin.html', {"form": form})

  def post(self, request):
    form = UserSignInForm(request.POST)
    username = request.POST['username']
    password = request.POST['password']

    if form.is_valid():
      user = authenticate(request, **form.cleaned_data)

      if user is not None:
        if user.is_active: 
          login(request, user)
          messages.success(request, "Welcome back!")
          return HttpResponseRedirect('/')
      else:
        messages.error(request, "Wrong username/email/password")
        return render(request, 'users/signin.html', {"form": form})
    
    return render(request, 'users/signin.html', {"form": form})