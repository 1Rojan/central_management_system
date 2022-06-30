"""project URL Configuration

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
from server import views as server_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servers/', server_views.list_server, name='server_list'),
    path('search/', server_views.search_server, name='search_server'),
    path('add_server/', server_views.add_server, name='add_server'),
    path('server/<int:server_id>/', server_views.server_detail_view, name='server_detail'),
    path('server/<int:server_id>/edit', server_views.update_server, name='update_server'),
    path('server/<int:server_id>/delete', server_views.delete_server, name='delete_server'),
    path("register", server_views.signup, name="register"),
    path("", server_views.login_request, name="login"),
    path("logout/", server_views.logout_request, name= "logout"),
]
