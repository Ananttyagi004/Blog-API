from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    cateogry=(
              ('Web-dev','Web-dev'),
              ('Machine Learning','Machine Learning'),
              ('App Dev','App Dev')
              )
    title= models.CharField(max_length=100)
    description=models.TextField()
    content= models.TextField()
    date_posted=models.DateField()
    category= models.CharField(max_length=160,null=True,choices=cateogry, default='Web-dev')
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    def __str__(self):
        return self.title