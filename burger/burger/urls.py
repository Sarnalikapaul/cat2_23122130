"""
URL configuration for burger project.

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
from burgerapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("employee/", employee, name="employee"),
    path("add/", add_employee, name="add_employee"),
    path("edit/<int:employee_id>/", edit_employee, name="edit_employee"),
    path("", login_view, name="login"),
    path("create_user/", create_user, name="create_user"),
    path(
        "employees/<int:employee_id>/delete/", delete_employee, name="delete_employee"
    ),
]
