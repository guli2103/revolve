from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

def index(request):
    postts = Post1.objects.all()
    context = {
        'postts' : postts
    }
    return render(request, 'index.html',context)








