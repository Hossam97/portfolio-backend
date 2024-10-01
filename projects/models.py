from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField('Name', max_length=500)
    icon = models.ImageField('Icon', upload_to='media/icons/techs/', null=True, blank=True)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    status_choices = [
        ('finished', 'Finished'),
        ('in_progress', 'Still in progress')
    ]
    title = models.CharField('Project title', max_length=200)
    desc = models.CharField('Project description', max_length=500)
    github = models.CharField('Github repo', max_length=100)
    href = models.CharField('Link to live demo (if any)', null=True, blank=True, max_length=100)
    img = models.ImageField('Image', upload_to='media/images/projects/', null=True, blank=True)
    status = models.CharField('Project status', default="finished", choices=status_choices, max_length=50)
    techStack = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        return self.title

