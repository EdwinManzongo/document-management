"""authservice URL Configuration

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
from django.urls import path, include
from home import urls as home_urls
from cabinet import urls as cabinet_urls
from students import urls as student_urls
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework import routers
from api import views
from rest_framework.authtoken import views as token_views

router = routers.DefaultRouter()

router.register(r'accounts', views.AccountViewSet)
# router.register(r'viewpickup', views.DetailedPickupViewSet ,basename = "IncidentCallout")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls, namespace="home")),
    path('cabinet/', include(cabinet_urls, namespace="cabinet")),
    path('student/', include(student_urls, namespace="student")),
    # path('admin/defender/', include('defender.urls')), # bruteforce defender 
    # path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'DMS System'
admin.site.site_title = 'DMS'
admin.site.site_url = ""
