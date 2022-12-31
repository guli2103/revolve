from django.urls import path
from backend.views import *

urlpatterns = [
   path('', index , name='index'),
   path('about/', AboutView.as_view() , name='about'),
   path('contact/', ContactView.as_view(), name='contact'),
   path('fashion/', CategoryView.as_view(), name='fashion'),
   path('index2/', Home2View.as_view(), name='index2'),
   path('index3/', Home3View.as_view(), name='index3'),
   path('index4/', Home4View.as_view(), name='index4'),
   path('index5/', Home5View.as_view(), name='index5'),
   path('index6/', Home6View.as_view(), name='index6'),
   path('post-audio/', PostaudioView.as_view(), name='post-audio'),
   path('post-gallery/', PostgalleryView.as_view(), name='post-gallery'),
   path('post-image/', PostimageView.as_view(), name= 'post-image'), 
   path('post-link/', PostlinkView.as_view(), name='post-link'),
   path('post-video/', PostvideoView.as_view(), name='post-video'),
   path('standard-fullwidth/', StandardfullView.as_view(), name='standard-fullwidth'),
   path('standard-left/', StandardleftView.as_view(), name='standard-left'),
   path('standard-right/',StandardrightView.as_view(), name='standard-right'),
]
