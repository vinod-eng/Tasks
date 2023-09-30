from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("vinod", views.vinod, name="vinod"),
    path("<str:name>", views.greet, name="greet")
    
]