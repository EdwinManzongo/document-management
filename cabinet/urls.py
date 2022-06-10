from django.urls import path
from cabinet import views
app_name = 'cabinet'
urlpatterns = [ 
    path('create_document', views.CreateDocument.as_view() , name="create_document"),
    # path('list_documents', views.ListDocuments.as_view() , name="list_documents"),
    path('list_documents', views.supervisor_dashboard , name="list_documents"),
    path('view_document/<pk>', views.DocumentDetailView.as_view() , name="view_document"),
    path('edit_document/<pk>', views.UpdateDocument.as_view() , name="edit_document"),
    path('review_document/<pk>', views.ReviewDocument.as_view() , name="review_document"),
    # Create Proposals
    path('upload_proposal', views.CreateProposal.as_view() , name="upload_proposal"),
    path('list_proposals', views.ListProposal.as_view() , name="list_proposals"),
    # path('client_delete/<pk>', views.DeleteClient.as_view() , name="client_delete"),
    # # FBV
    # path('search_document', views.search_document , name="search_document"),
    # path('document_filter', views.document_filter , name="document_filter"),
    # path('function_data', views.function_data , name="function_data"),
]