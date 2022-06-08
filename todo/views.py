from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem, Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin



first_time = True

# Create your views here.
def todoView(request):
  global first_time
  all_todo_items = TodoItem.objects.all()
  if (first_time):
      new_item = TodoItem(content = "build a cool app on replit.com")
      new_item.save()
      first_time = False
  return render(request, 'index.html', 
  {'all_items': all_todo_items})

def addTodo(request):
  new_item = TodoItem(content = request.POST['content'])
  new_item.save()
  return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
  item_to_delete = TodoItem.objects.get(id=todo_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')


def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def homePage(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'mysite/home.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def videoPage(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'mysite/video.html', {'tasks': tasks})

def borodinPage(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'mysite/borodin.html', {'tasks': tasks})

def loginPage(request):
  return render(request, 'registration/login.html')

def telegramPage(request):
  return render(request, 'mysite/telegram.html')

def createPage(request, slug):
  error  = ''
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else: 
      error = 'Форма была неверной.'
  form = TaskForm()
  context = {
    'form': form,
    'error': error
  }
  return render(request, 'mysite/create.html', context)
