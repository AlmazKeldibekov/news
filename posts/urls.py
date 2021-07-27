"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from posts.views import (posts_list_view, post_detail_view,
                         PostCreateView, PostUpdateView, PostDeleteView)

urlpatterns = [
    path('', posts_list_view, name='posts_list_url'),
    path('<int:id>/', post_detail_view, name='post_detail_url'),
    path('create/', PostCreateView.as_view(), name='post_create_url'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update_url'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete_url'),
]
