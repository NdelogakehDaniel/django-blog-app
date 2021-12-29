from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "category"
    
class Post(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to="images/")
    views = models.IntegerField(default=0)    
    likes = models.IntegerField(default=0) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)   

    class Meta:
        db_table = "posts"