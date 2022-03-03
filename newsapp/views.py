from itertools import count
from unicodedata import category
from django.shortcuts import render
from django.views.generic import View, TemplateView

from newsapp.models import Catagories, News
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        All_news = News.objects.all().order_by("-id")
        # title = news_objs.news_title
        count = 2
        context['All_news'] = All_news
       
        categories = Catagories.objects.all()
        context['categories'] = categories
        print('------------',categories)
        
        return context
    

class DetailView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['pk']
        
        news = News.objects.get(id = pk)
        
        context['news'] = news
     
        
        
        return context
class CategoriesView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catagories = Catagories.objects.all()
        
        context['catagories'] = catagories
        return context
    
class CategoryView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        pk = kwargs['pk']
        
        cid = Catagories.objects.get(id = pk)
        news = cid.news_set.all()
        # print(news,'[[[[[[[[[[[[[[[[[[[[[[[[[[[[')
        context['news'] = news
        context['cid'] = cid
        
        return context