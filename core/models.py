from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

DIAGNOSIS_CHOICES = (
   ("", "Select Diagnosis"),
  ("anxiety", "Anxiety"),
  ("asthma", "Asthma"),
  ("arthritis", "Arthritis"),
  ("back pain", "Back pain"),
  ("cirrhosis", "Cirrhosis"),
  ("cough", "Cough"),
  ("cold and catarrh", "Cold and Catarrh"),
  ("coronavirus", "Coronavirus"),
  ("diabetes", "Diabetes"),
  ("hay fever", "Hay fever"),
  ("headache", "Headache"),
  ("hypertension", "Hypertension"),
  ("hyperlipidemia", "Hyperlipidemia"),
  ("hiv", "HIV"),
  ("kidney stone", "Kidney stone"),
  ("malaria", "Malaria"),
  ("nail fungus", "Nail fungus"),
  ("obsessive compulsive disorder", "Obsessive compulsive disorder (OCD)"),
  ("obesity", "Obesity"),
  ("pain in joint", "Pain in joint"),
  ("pneumonia", "Pneumonia"),
  ("respiratory problems", "Respiratory problems"),
  ("scabies", "Scabies"),
  ("typhoid", "Typhoid"),
  ("ulcer", "Ulcer"),
  ("whooping cough", "Whooping cough"),
  ("yellow fever", "Yellow fever"),

)

BLOOD_GROUP_CHOICES = (
  ("", "Select Blood Group"),
  ("A+", "A+"),
  ("A-", "A-"),
  ("B+", "B+"),
  ("AB+", "AB+"),
  ("AB-", "AB-"),
  ("O+", "O+"),
  ("O-", "O-"),
)

class MedicalInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='medical_info')
  blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
  diagnosis = models.CharField(max_length=30, choices=DIAGNOSIS_CHOICES)
  vital_signs = models.CharField(max_length=255)
  medications = models.CharField(max_length=200)
  allergies = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.user.username