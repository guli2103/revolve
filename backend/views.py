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

class Home2View(TemplateView):
    template_name = 'index-2.html';   

class Home3View(TemplateView):
    template_name = 'index-3.html';

class Home4View(TemplateView):
    template_name = 'index-4.html';

class Home5View(TemplateView):
    template_name = 'index-5.html';    

class Home6View(TemplateView):
    template_name = 'index-6.html';   

class PostaudioView(TemplateView):
    template_name = 'post-audio.html';

class PostgalleryView(TemplateView):
    template_name = 'post-gallery.html'; 

class PostimageView(TemplateView):
    template_name = 'post-image.html'; 

class PostlinkView(TemplateView):
    template_name = 'post-link.html';

class PostvideoView(TemplateView):
    template_name = 'post-video.html'; 

class StandardfullView(TemplateView):
    template_name = 'standard-fullwidth.html';   

class StandardleftView(TemplateView):
    template_name = 'standard-left-sidebar.html';            

class StandardrightView(TemplateView):
    template_name = 'standard-right-sidebar.html';













