from django.urls import path
from data import views

urlpatterns = [
    path('create/', views.index,name='index'),
    path('delete/',views.delete,name='delete')
]
