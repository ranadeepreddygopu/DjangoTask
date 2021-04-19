from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Task(models.Model):
    Name = models.CharField(null= True,max_length=20)
    Phone = models.CharField(null=True,max_length=20,validators=[RegexValidator(regex ='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$',message = 'Enter Valid Number')])
    URLField = models.URLField(max_length = 200)
