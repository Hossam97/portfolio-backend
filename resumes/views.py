from resumes.models import Resume
from django.http import Http404
from django.http.response import JsonResponse

# Create your views here.
def getMostRecentResume(req):
    resume = Resume.objects.all().order_by('id').last()
    if resume is not None:
        return JsonResponse({'file_path': resume.file.url})
    else:
        return Http404('File does not exist')