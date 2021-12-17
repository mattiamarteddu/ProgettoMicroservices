"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from Books import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookList.as_view()),
    path('<int:book_id>/', views.BookGet.as_view()),
    path("create/", views.BookCreate.as_view(), name="Book_create"),
    path("update/<int:pk>/", views.BookUpdate.as_view(), name="update_Book"),
    path("delete/<int:pk>/", views.BookDelete.as_view(), name="delete_Book"),

]
