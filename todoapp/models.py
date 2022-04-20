from django.db import models

# Create your models here.

class Todos(models.Model):
  task_name=models.CharField(max_length=120)
  user=models.CharField(max_length=80)
  date=models.DateField(auto_now_add=True)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.task_name


#ORM queries
#object -relational mapper
#ORM query for creating resource
#ref_name=Modelname(fieldname="value")
#ref_name.save()

#or
#modelname.objects.create(fieldname="value")

#orm query for fetching all records
#ref name=model name.objects.all()
#qs=Todos.objects.all()

#orm queries for filtering,excluding,to get a specific value
#ref_name=modelname.objects.filter(fieldname="value")

#ref_name=modelname.objects.all().exclude(fieldname="value")

#ref_name=modelname.objects.get(fieldname="value")