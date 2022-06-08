"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = 'todo'
from django.contrib import admin#, auth
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from todo.views import todoView, addTodo, deleteTodo, coverImage, homePage, videoPage, createPage, loginPage, borodinPage, telegramPage


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('accounts/', include('django.contrib.auth.urls')),
    path('', homePage, name='home'), #todoView
    #path('', include('login.urls')),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('app.png', coverImage),
    path('video', videoPage, name='video'),
    path('borodin', borodinPage, name='borodin'),
    path('telegram', telegramPage, name='telegram'),
    #path('login',loginPage, name='login'),
    path('create', createPage, name='create'),
    path('<slug:slug>/', createPage, name='page'),
    #path('', include('todo.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
]


urlpatterns += i18n_patterns(
    path('', homePage, name='home'),
    path('video', videoPage, name='video'),
    path('borodin', borodinPage, name='borodin'),
    path('telegram', telegramPage, name='telegram'),
    path('create', createPage, name='create'),
  
)