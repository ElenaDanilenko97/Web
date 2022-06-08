from django.contrib import admin
from . models import Task
from . models import Composer
# Register your models here.


admin.site.register(Task)
admin.site.register(Composer)

class ComposerAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}