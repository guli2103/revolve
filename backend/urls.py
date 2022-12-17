from django.urls import path
from backend.views import *

urlpatterns = [
   path('', index),
   path('about/', AboutView.as_view() , name='about'),
   path('contact/', ContactView.as_view(), name='contact'),
   path('fashion/', CategoryView.as_view(), name='fashion'),
   path('index2/', Home2View.as_view(), name='index2')
]
