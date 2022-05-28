from django.urls import path
from api import views
from django.contrib.auth.decorators import login_required
app_name = 'api-app'
urlpatterns = [ 
    # path('list-request', login_required(views.BookWash.as_view()), name="create_vehicle_booking"),
]


