from django.urls import path
from .views import projects_index, project_details

urlpatterns = [
    path('', projects_index, name='projects_index'),
    path("<int:pk>/", project_details, name="project_details"),
]
