from itertools import count
from django.shortcuts import render
from django.views.generic import View, TemplateView

from newsapp.models import News
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        All_news = News.objects.all().order_by("-id")
        # title = news_objs.news_title
        count = 2
        context['All_news'] = All_news
        context['count'] = count
        
        return context
    
class DetailView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['pk']
        
        news = News.objects.get(id = pk)
        
        context['news'] = news
        
        
        return context