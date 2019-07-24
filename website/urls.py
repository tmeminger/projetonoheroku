from django.urls import path, include
from website.views import index, sobre

urlpatterns = [
    path('', index),
    path('sobre', sobre)
]
