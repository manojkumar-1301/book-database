"""phoenix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from BookStore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User', views.User, name='User'),
    path('Book',views.Book,name='Book'),
    path('Order',views.Order,name='Order' ),
    path('login',views.login,name='login'),
    path('ShowBook',views.ShowBook,name='ShowBook'),
    path('ShowUser',views.ShowUser,name='ShowUser'),
    path('ShowOrder',views.ShowOrder,name='ShowOrder'),
    path('add_order',views.add_order,name='add_order'),
    path('add_book',views.add_book,name='add_book'),
    path('sorder',views.sorder,name='sorder'),
    path('sbook',views.sbook,name='sbook'),
    path('newacc',views.newacc,name='newacc'),
    path('edit/(?P<pk>\d+)/$',views.edit,name='edit'),
    path('oedit/(?P<pk>\d+)/$', views.oedit, name='oedit'),
    path('uedit/(?P<pk>\d+)/$', views.uedit, name='uedit'),
    path('delete/(?P<pk>\d+)/$',views.delete,name='delete'),
    path('odelete/(?P<pk>\d+)/$',views.odelete,name='odelete'),
    path('udelete/(?P<pk>\d+)/$',views.udelete,name='udelete'),
]
