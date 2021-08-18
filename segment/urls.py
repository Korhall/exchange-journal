from django.urls import path, include
from .views import mainindex

urlpatterns = [
    path('', mainindex, name='mainindex'),
    

]