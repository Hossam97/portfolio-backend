from django.urls import include, path
from projects.views import getProject, getAllProjects
urlpatterns = [
    path("", getAllProjects, name="projects-view"),
    path("<int:id>", getProject, name="project-view"),
    ]
