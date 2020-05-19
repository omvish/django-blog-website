from django.db import models
from datetime import datetime
# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'images/') #automatically ceated through media paths
    description = models.CharField(max_length = 10000, default = '')
    author = models.CharField(max_length = 100 )
    upload_date = models.DateTimeField(default=datetime.now, blank=True) #by deafult false
