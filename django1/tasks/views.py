from django1.settings import LOGIN_REDIRECT_URL
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import Task, TaskForm
from django.contrib import messages
import datetime


@login_required
def taskList(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Task.objects.filter(status='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    tasksDone = Task.objects.filter(status='done', user=request.user).count()
    tasksDoing = Task.objects.filter(status='doing', user=request.user).count()

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    
    elif filter:
        tasks = Task.objects.filter(status=filter, user=request.user)
    
    else:
        task_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(task_list, 3)
        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks':tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'doing'
            task.user = request.user
            task.save()
            messages.info(request, 'Nova tarefa adicionada')
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form' : form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            messages.info(request, 'Tarefa editada com sucesso')

            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form':form, 'task':task})
    else:
        return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)
    if task.status == 'doing':
        task.status = 'done'
    else:
        task.status = 'doing'

    task.save()
    return redirect('/')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

def helloWorld(request):
    return HttpResponse('Hello World!')