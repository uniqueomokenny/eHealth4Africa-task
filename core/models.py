from django.db import models
from django.contrib.auth import get_user_model

from .input_choices import BLOOD_GROUP_CHOICES, DIAGNOSIS_CHOICES

User = get_user_model()



class MedicalInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medical_info')
  blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
  diagnosis = models.CharField(max_length=30, choices=DIAGNOSIS_CHOICES)
  vital_signs = models.CharField(max_length=255)
  medications = models.CharField(max_length=200)
  allergies = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.user.username