from django.urls import path
from resumes.views import getMostRecentResume
urlpatterns = [
    path('last-resume', getMostRecentResume, name="latest-resume-view")
]