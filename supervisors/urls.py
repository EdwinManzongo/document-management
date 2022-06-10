from django.urls import path
from supervisors import views
app_name = 'supervisors'

urlpatterns = [ 
    path('create_supervisor', views.CreateSupervisor.as_view() , name="create_supervisor"),
    path('list_supervisor', views.ListSupervisors.as_view() , name="list_supervisor"),
    path('view_supervisor/<pk>', views.SupervisorsDetailView.as_view() , name="view_supervisor"),
    path('edit_supervisor/<pk>', views.UpdateSupervisor.as_view() , name="edit_supervisor"),
    # path('client_delete/<pk>', views.DeleteClient.as_view() , name="client_delete"),
    # Students URLs
    path('list_students', views.ListStudents.as_view() , name="list_students"),
    path('view_profile/<pk>', views.StudentsDetailView.as_view() , name="view_profile"),
    path('edit_profile/<pk>', views.UpdateStudent.as_view() , name="edit_profile"),
]