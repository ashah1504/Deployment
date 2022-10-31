from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from tasks.forms import Taskforms


def contacts(request):
    return render(request, 'taskapp/contact.html')


def home(request):
    return render(request, 'taskapp/home.html')


def post(request):
    return render(request, 'taskapp/post.html')


def tasks(request):
    return render(request, 'taskapp/tasks.html')


def taskadd(request):
    form = Taskforms()
    if request.method == 'POST':
        myData = Taskforms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request, 'Task Added Successfully')
            return redirect('tasks')
    context = {"form": form}
    return render(request, 'taskapp/taskadd.html', context)


def profile(request):
    return render(request, 'taskapp/profile.html')
