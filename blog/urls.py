from django.urls import path
from . import views

app_name = 'blogweb'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('blogs', views.posts_list, name='posts_list'),
    path('<slug:category_slug>', views.posts_list, name='posts_by_category'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]