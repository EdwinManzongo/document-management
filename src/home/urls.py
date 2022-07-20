from django.conf.urls import url
from django.urls import path 
from home import views
from django.contrib.auth.decorators import login_required
app_name = 'home'
urlpatterns = [ 
    path('', views.home_login , name="login"),
    path('logout', views.home_logout, name="logout"),
    path('create_account', views.CreateAccount.as_view(), name="create_account"),
    path('list_accounts', views.ListAccounts.as_view(), name="list_accounts"),
]
