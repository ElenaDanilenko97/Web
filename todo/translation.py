from modeltranslation.translator import register, TranslationOptions
from .models import Task

@register(Task)
class TaskTranslationOptions(TranslationOptions):
  fields = ('title', 'task')