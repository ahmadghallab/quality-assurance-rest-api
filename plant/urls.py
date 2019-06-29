from django.urls import path

from . import views

app_name = 'plant'

urlpatterns = [
    path('management/', 
        views.ListCreateManagement.as_view()),
    path('management/<int:pk>/',
        views.RetrieveUpdateDestroyManagement.as_view()),
    path('unit/',
        views.ListCreateUnit.as_view()),
    path('unit/<int:pk>/',
        views.RetrieveUpdateDestroyUnit.as_view()),
]