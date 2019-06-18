"""e_bukutamu URL Configuration

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
from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'pelaporan'

urlpatterns = [
    path('', views.index, name='index'),
    path('bukutamu', views.bukutamu, name='bukutamu'),
    path('users', views.users, name='users'),
    path('users/<int:pk>', views.users_detail, name='users_detail'),
    path('ajax/<int:uid>', views.get_tamu, name='ajax_users_detail'),
    path('lapor', views.lapor, name = 'lapor'),
    path('submit', views.submit, name = 'submit'),
    path('listlapor', views.list_pelaporan, name = 'listlapor'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('test', views.test, name = 'test'),
]
