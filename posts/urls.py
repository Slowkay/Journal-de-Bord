from django.urls import path
from . import views
from .views import FolderDeleteView, PostDeleteView

"""
L11 : 'post/<int:pk>/edit/' : Partie de l'URL à laquelle renvoit cette view 
ex : https://robinguesdon-blog/post/2/edit/ (ici 2 correspond à la clé primaire de l'article du blog qu'on veut éditer)

'views.post_edit' : Correspond à la view qui va être utilisée pour afficher cette page. 
Ex : 'def post_edit()' dans le fichier views.py

name='post_edit' : Nom que l'on donne à ce path(chemin). On s'en servira pour construire une URL dans un template. 
Ex : <h1><a href="{% url 'post_list' %}">Django Girls Blog</a></h1>
"""

urlpatterns = [
    path('', views.folder_list, name='folder_list'), 
    path('folder/<int:folder_pk>/', views.post_list, name='post_list'), 
    path('folder/new/', views.folder_new, name='folder_new'),
    path('folder/post/new/', views.post_new, name='post_new'),    
    path('folder/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('folder/<int:pk>/edit/', views.folder_edit, name='folder_edit'),  
    path('folder/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('folder/delete/<int:pk>/', FolderDeleteView.as_view(), name='folder_delete'),
    path('folder/post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]