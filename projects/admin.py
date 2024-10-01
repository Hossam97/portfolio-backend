from django.contrib import admin
from projects.models import Project, Technology

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'github', 'href', 'img', 'status']
    raw_id_fields = ['techStack']

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon']

