from django.shortcuts import render, redirect 
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404


def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('index')

def toggle(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')
