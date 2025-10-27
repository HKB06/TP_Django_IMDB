"""
URL configuration for minigallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from gallery.views import gallery_list, add_image, upload_to_imgur

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gallery_list, name='gallery_list'),
    path('add/', add_image, name='add_image'),
    path('upload/', upload_to_imgur, name='upload_image'),
]
