from django.shortcuts import render
from .forms import FitnessForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# render welcome page
def index(request):
    return render(request, 'cwApp/index.html')


# import/ render form
def createUser(request):
    form = FitnessForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'cwApp/newUser.html', context)


# save form info and return confirmation
def addUser(request):
    User.objects.create_user(request.POST['username'], '', request.POST['password'])
    return HttpResponse('new user created')
