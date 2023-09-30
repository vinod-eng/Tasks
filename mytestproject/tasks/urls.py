from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path('show-session/', views.show_session_data, name='show_session_data'),
    path('delete/<int:task_id>', csrf_exempt(views.delete), name="delete")
]