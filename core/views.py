from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.http import HttpResponseRedirect


from .models import MedicalInfo
from .forms import AddMedicalInfoForm

class HomeView(TemplateView):
  template_name='core/home.html'

class MedicalInfoView(View):
  def get(self, request):
    form = AddMedicalInfoForm()
    return render(request, 'core/add-medical-info.html', {"form": form})

  def post(self, request):
    form = AddMedicalInfoForm(request.POST)

    if form.is_valid():
      user = request.user

      medical_info = MedicalInfo.objects.create(user=user, **form.cleaned_data)

      messages.success(request, "You successfully added your medical info.")
      return HttpResponseRedirect('/')
    else:
        messages.error(request, "Invalid data")
        return render(request, 'core/add-medical-info.html', {"form": form})
    
    return render(request, 'core/add-medical-info.html', {"form": form})
