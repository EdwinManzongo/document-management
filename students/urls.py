from django.urls import path
from students import views
app_name = 'students'

urlpatterns = [ 
    path('create_profile', views.CreateStudent.as_view() , name="create_profile"),
    path('list_profile', views.ListStudents.as_view() , name="list_profile"),
    path('view_profile/<pk>', views.StudentsDetailView.as_view() , name="view_profile"),
    path('edit_profile/<pk>', views.Update_Student.as_view() , name="edit_profile"),
    # path('client_delete/<pk>', views.DeleteClient.as_view() , name="client_delete"),
]