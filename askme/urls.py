"""askme URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views
from askme import settings

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('login/', views.login, name='login'),
    path('tag/python/', views.tag, name='tag'),
    path('settings/', views.settings, name='settings'),
    path('hot/', views.hot, name='hot'),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.pageNotFound
