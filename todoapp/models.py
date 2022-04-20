from django.db import models

# Create your models here.

class Todos(models.Model):
  task_name=models.CharField(max_length=120)
  user=models.CharField(max_length=80)
  date=models.DateField(auto_now_add=True)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.task_name

#orm query for fetching all records
#ref name=model name.objects.all()
#qs=Todos.objects.all()