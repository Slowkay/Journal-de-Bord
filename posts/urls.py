from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # name='post_list' --> nom de l'URL qui sera utilisée afin d'identifier la vue
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]