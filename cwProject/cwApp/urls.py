from django.urls import path
from . import views

urlpatterns = [
    # index page
    path('', views.index, name='index'),
    # create a user (accessed through link)
    path('createUser/', views.createUser, name='newUser'),
    # add a user (accessed through form submission)
    path('addUser/', views.addUser, name='addUser'),
]
