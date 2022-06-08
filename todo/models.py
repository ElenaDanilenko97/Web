from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class TodoItem(models.Model):
  content = models.TextField()


class Task(models.Model):
  title = models.CharField('Тема', max_length=50)
  task = models.TextField('Комментарий')
  created_date = models.DateTimeField('time', default=timezone.now)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "Комментарий"
    verbose_name_plural = "Комментарии"

def slug_default():
  return {"slug": "ttt"}
   
class Composer(models.Model):
  name = models.CharField('name',max_length=200)
  slug = models.SlugField('slug', unique=True, default=slug_default)
  text = models.TextField('text')

 
    
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('')


