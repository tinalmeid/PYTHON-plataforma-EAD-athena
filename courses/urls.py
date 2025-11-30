from django.urls import path
from . import views

app_name = 'courses' # Namespace for the 'courses:index'

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index view
    path('<slug:slug>/', views.detail, name='detail'),  # URL for the detail view
]
