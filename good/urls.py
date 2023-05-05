"""good URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.urls import re_path as url
from django.conf import settings
from goods import views
from user import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', user_views.login,name='login'),
    url(r'^register/', user_views.register,name='register'),
    url(r'^logout/', user_views.logout, name='logout'),
    url(r'^purchase', views.purchase, name='purchase'),
    url(r'^cancellation', views.cancellation, name='cancellation'),
    url(r'^index/', views.index, name='index'),
    url(r'^order/', views.order, name='order'),
    url('', views.index, name='index'),
    url(r'register/', views.index,name='register'),
    url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
