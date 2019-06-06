"""todo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    
    # path('', views.TalkList.as_view()), # empty api/ wud show all the talks 
    # path('<int:pk>/', views.TalkDetail.as_view()),#api/# wud show tht specific talk with its id
    # path( '<int:pk>/', views.talk_detail, name='GetTalk'),
    # path( '', views.talk_list, name='get_post_talk'),
    path( 'gettalks', views.GetTalks, name='GetTalks'),
    path( 'gettalks/<int:pk>', views.GetTalk, name='GetTalk'),
    path( 'insert', views.Insert, name='Insert'),
    path( 'update', views.Update, name='Update'),
    path( 'delete/<int:pk>', views.Delete, name='Delete'),
]