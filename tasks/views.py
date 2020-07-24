from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk): 
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST': 
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST': 
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def where(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/where.html', context)

def when(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/when.html', context)

def project(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/project.html', context)

def area(request):    
    area = Area.objects.all()
    form = AreaForm()

    if request.method =='POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks/area.html')

    context = {'area':area, 'form':form}
    return render(request, 'tasks/area.html', context)
