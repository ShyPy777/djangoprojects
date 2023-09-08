"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from book import views
app_name = "book"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),#http:127.0.0.1:8000
    path('addbook',views.addbook,name='addbook'),#http:127.0.0.1:8000/index
    path('addbook1',views.addbook1,name='addbook1'),
    path('addstudents',views.addstudents,name='addstudents'),
    path('addstudents1',views.addstudents1,name='addstudents1'),
    path('viewbookdetails',views.viewbookdetails,name='viewbookdetails'),#http:127.0.0.1:8000/viewbook
    path('view/<int:p>/',views.view,name='view'),
    path('delete/<int:p>/',views.delete,name='delete'),
    path('edit/<int:p>/', views.edit, name='edit'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('fact',views.fact,name='fact'),
]