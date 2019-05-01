from django.urls import path
from . import views

app_name = 'upload_profile'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # upload image
    path('add/', views.add, name='add'),
    # recognize face
    path('recognize/', views.recognize, name='recognize'),
]