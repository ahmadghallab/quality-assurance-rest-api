from django.urls import path

from . import views

app_name = 'plant'

urlpatterns = [
    path('management', 
        views.ListCreateManagement.as_view()),
    path('management/<int:pk>',
        views.RetrieveUpdateDestroyManagement.as_view()),

    path('unit',
        views.ListCreateUnit.as_view()),
    path('unit/<int:pk>',
        views.RetrieveUpdateDestroyUnit.as_view()),

    path('department', 
        views.ListCreateDepartment.as_view()),
    path('department/<int:pk>',
        views.RetrieveUpdateDestroyDepartment.as_view()),

    path('section',
        views.ListCreateSection.as_view()),
    path('section/<int:pk>',
        views.RetrieveUpdateDestroySection.as_view()),

    path('criterion',
        views.ListCreateCriterion.as_view()),
    path('criterion/<int:pk>',
        views.RetrieveUpdateDestroyCriterion.as_view())
]