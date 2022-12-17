from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

def index(request):
    postts = Post1.objects.all()
    context = {
        'postts' : postts
    }
    return render(request, 'index.html',context)

class AboutView(TemplateView):
    template_name = 'about.html';


class ContactView(TemplateView):
    template_name = 'contact.html';    


class CategoryView(TemplateView):
    template_name = 'fashion.html';









