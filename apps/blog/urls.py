from django.urls import path
from .views import blog_index, blog_detail, blog_category

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("<int:pk>/", blog_detail, name="blog_detail"),
    path("<category>/", blog_category, name="blog_category"),
]
