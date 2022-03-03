from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Catagories(models.Model):
    cg_name = models.CharField(max_length=200)
    cg_descriptions = models.TextField()
    img = models.ImageField(upload_to = 'cat_img')
   
    def __str__(self):
        return self.cg_name
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    username  = models.CharField(max_length=50)
    author_img = models.ImageField(upload_to = 'author_img')
    
   
    def __str__(self):
        return self.name
  

class News(models.Model):

    catagory = models.ForeignKey(Catagories, on_delete=models.CASCADE)    
    img = models.ImageField(upload_to = 'news_img')  
    date_posted = models.DateTimeField(auto_now_add=True)
    news_title = models.CharField(max_length=200) 
    news_content = models.TextField()
    date_updated = models.DateTimeField(auto_now=True) 
    news_status = models.BooleanField(default=False)  
    comment_status = models.BooleanField(default=False) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    
    
   
    def __str__(self):
        return self.news_title
    
    
class Sub_New(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=200)
    sub_description = models.TextField()  
    img = models.ImageField(upload_to = 'Sub_img')
      
    def __str__(self):
        return self.news.news_title + '(' +  self.sub_title  + ')'
