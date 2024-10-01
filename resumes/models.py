from django.db import models

# Create your models here.
class Resume(models.Model):
    file = models.FileField('Resume file', upload_to='media/files/resumes')