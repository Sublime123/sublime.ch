from django.urls import path,re_path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('thread', views.thread, name='thread'),
    path('board', views.board, name='board'),
    #path('thread', views.thread, name='thread'),
    
    #path('send', views.send, name='send'),
    #path('add', views.add, name='add')
]