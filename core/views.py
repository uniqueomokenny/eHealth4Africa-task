from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


from .models import MedicalInfo
from .forms import AddMedicalInfoForm
from .decorators import medical_practioner_login_required
from .input_choices import DIAGNOSIS_CHOICES

class HomeView(LoginRequiredMixin, TemplateView):
  template_name='core/home.html'

  def get(self, request, *args, **kwargs):
    user_medical_info = MedicalInfo.objects.filter(user=request.user).first()

    context = self.get_context_data(**kwargs)
    context["user_medical_info"] = user_medical_info
    return self.render_to_response(context)

class MedicalInfoView(LoginRequiredMixin, View):
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


@login_required
def statistical_details(request):
  medical_recodes = MedicalInfo.objects.all()
  medical_info = []
  for recode in medical_recodes:
    medical_info.append({
      "diagnosis": recode.get_diagnosis_display()
    })

  return render(request, 'core/statistical-details.html', {"medical_info": medical_info})

@medical_practioner_login_required
def medical_recodes(request):
  query = request.GET.get('q')
  medical_recodes = MedicalInfo.objects.all()
  if query is not None:
    medical_recodes = MedicalInfo.objects.filter(diagnosis=query)
    if query == '':
      medical_recodes = MedicalInfo.objects.all()

  context =  {
    "medical_recodes": medical_recodes,
    'diagnosis_choices': DIAGNOSIS_CHOICES,
    "query": query
  }
  return render(request, 'core/medical-recodes.html', context)