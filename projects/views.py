from django.http import Http404
from django.http.response import JsonResponse
from projects.models import Project
from projects.serializers import ProjectSerializer
# Create your views here.

def getProject(req, id):
    project = Project.objects.get(pk=id)
    if project is not None:
        return JsonResponse(ProjectSerializer(project).data)
    else:
        return Http404('Project does not exist')
    
def getAllProjects(req):
    projects = Project.objects.all().order_by('-id')[:4]
    if projects is not None:
        return JsonResponse(ProjectSerializer(projects, many=True).data, safe=False)
    else:
        return Http404('No projects yet!')

    