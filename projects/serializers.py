from rest_framework import serializers
from projects.models import Project, Technology

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name', 'icon']

class ProjectSerializer(serializers.ModelSerializer):
    techStack = TechnologySerializer(many=True)
    
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'desc',
            'github',
            'href',
            'status',
            'img',
            'techStack'
        ]