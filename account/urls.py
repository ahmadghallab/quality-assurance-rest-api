from django.urls import path

from . import views

app_name = 'account'
 
urlpatterns = [
    path('create/',
        views.CreateUser.as_view()),
    path('<int:pk>/',
        views.RetrieveUpdateDestroyUser.as_view()),
    path('auth/',
        views.CustomAuthToken.as_view()),
]