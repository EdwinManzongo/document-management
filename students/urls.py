from django.urls import path
from students import views
app_name = 'students'

urlpatterns = [ 
    path('create_profile', views.CreateStudent.as_view() , name="create_profile"),
    path('list_profile', views.ListStudents.as_view() , name="list_profile"),
    path('view_profile/<pk>', views.StudentsDetailView.as_view() , name="view_profile"),
    path('edit_profile/<pk>', views.UpdateStudent.as_view() , name="edit_profile"),
    path('profile_delete/<pk>', views.DeleteStudent.as_view() , name="profile_delete"),
    # Document URLs
    path('create_document', views.CreateDocument.as_view() , name="create_document"),
    path('list_documents', views.student_dashboard , name="list_documents"),
    # path('list_documents', views.ListDocuments.as_view() , name="list_documents"),
    path('view_document/<pk>', views.DocumentDetailView.as_view() , name="view_document"),
    path('edit_document/<pk>', views.UpdateDocument.as_view() , name="edit_document"),
    # Proposal URL
    path('list_proposals', views.ListProposal.as_view() , name="list_proposals"),
]