from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('thread/<thread_id>/', views.thread_view, name='thread_view'),
]
