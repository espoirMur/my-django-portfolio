from django.shortcuts import render
from .models import Project


def projects_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects_index.html', context)


def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'projects_details.html', context)
