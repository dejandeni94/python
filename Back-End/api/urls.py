
"""melonpdf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import UsersData
from .views import UsersDetails
from .views import ProjectsData
from .views import ProjectsDetails
from .views import FileUploadData


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls, name='Admin'),
    path('api/users',UsersData.as_view(),name='Users'),
    path('api/users/<int:pk>/',UsersDetails.as_view(),name='Users_ID'),
    path('api/users/<int:pk>/update/', UsersDetails.as_view(), name='Users update'),
    path('api/users/<int:pk>/delete/', UsersDetails.as_view(), name='Users delete'),
    path('api/projects',ProjectsData.as_view(),name='Projects'),
    path('api/projects/<int:pk>/',ProjectsDetails.as_view(),name='Project_ID'),
    path('api/projects/<int:pk>/update/', ProjectsDetails.as_view(), name='Project update'),
    path('api/projects/<int:pk>/delete/', ProjectsDetails.as_view(), name='Projects delete'),
    path('api/auth', include('rest_framework.urls')),
    path('api/upload/',FileUploadData.as_view(), name='Files Upload'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), 
]