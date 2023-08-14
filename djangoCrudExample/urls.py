"""djangoCrudExample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path , include
from crudapp import views
from djangoCrudExample import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path('admin/', admin.site.urls),
    
    path('contacts/', views.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>/', views.edit, name='edit'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/delete/<int:pk>/', views.delete, name='delete'),
    path('contacts/deleteClub/<int:pk>/', views.deleteClub, name='deleteClub'),
    path('contacts/deleteAct/<int:pk>/', views.deleteAct, name='deleteAct'),
    path('contacts/create_club/', views.createClub ,name='createClub'),
    path('contacts/edit_club/<int:pk>/', views.editClub ,name='editClub'),
    path('contacts/create_act/', views.createAct ,name='createAct'),
    path('contacts/edit_act/<int:pk>/', views.editAct ,name='editAct'),
    path('contacts/index_club/', views.IndexClub.as_view() ,name='IndexClub'),
    path('contacts/index_act/', views.IndexAct.as_view() ,name='IndexAct'),
    path('crudapp/', include('crudapp.urls')),
   
    

    #path('upload/', include('profile_maker.urls')),
    ]

"""if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]