from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DocumentCreateForm, DocumentEditForm, ProposalCreateForm
from .models import Cabinet, ProposalCabinet
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import date , datetime
from django.urls import reverse
from django.db.models import Q , Sum ,Count

from django.views.generic import (CreateView, DetailView, ListView, TemplateView, UpdateView )
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
# from clients.models import Client

# from .function_views import *

class CreateDocument(CreateView):
    model = Cabinet
    form_class = DocumentCreateForm
    template_name = 'cabinet/create_document.html'
    # success_url = '/list_documents'

    def form_valid(self, form): 
        data = form.save(commit=False)
        data.created_at = timezone.now()
        data.created_by = self.request.user.id
        data.user_name = self.request.user
        data.updated_at = timezone.now()
        data.save()

        # messages.add_message(self.request, messages.INFO, 'Document successfully saved')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('cabinet:list_documents', kwargs={})

class ListDocuments(ListView):
    model = Cabinet
    template_name = 'cabinet/list_documents.html'
    # clients = None
    def get_context_data(self, **kwargs):
        context = super(ListDocuments, self).get_context_data(**kwargs)
        # clients = Client.objects.all().order_by('fullname_or_company_name')
        
        context['title'] = "Listing Documents"
        # context['clients'] = clients
        return context

def supervisor_dashboard(request):
    all_calls = Cabinet.objects.filter(supervisor = request.user.id)

    context = {
        'title':'Your Documents',
        'all_calls': all_calls,
    }

    return render(request , "cabinet/list_documents.html" , context) 

class UpdateDocument(SuccessMessageMixin, UpdateView):
    model = Cabinet
    template_name = 'cabinet/update_document.html'
    form_class = DocumentEditForm
    # success_message = 'Document  updated'

    def get_context_data(self, **kwargs):
            context = super(UpdateDocument, self).get_context_data(**kwargs)
            context['title'] = "Updating information for Document no : "+str(self.kwargs['pk'])
            return context
            
    def get_success_url(self):
        return reverse('cabinet:list_documents', kwargs={})

class DocumentDetailView(DetailView):
    model = Cabinet
   
    template_name = "cabinet/view_document.html"

class ReviewDocument(SuccessMessageMixin, UpdateView):
    model = Cabinet
    template_name = 'cabinet/update_document.html'
    form_class = DocumentEditForm
    # success_message = 'Document  updated'

    def get_context_data(self, **kwargs):
            context = super(Update_Document, self).get_context_data(**kwargs)
            context['title'] = "Updating information for Document no : "+str(self.kwargs['pk'])
            return context
            
    def get_success_url(self):
        return reverse('cabinet:list_documents', kwargs={})

# Proposal Idea
class CreateProposal(CreateView):
    model = ProposalCabinet
    form_class = ProposalCreateForm
    template_name = 'cabinet/create_proposal.html'
    # success_url = '/list_documents'

    def form_valid(self, form): 
        data = form.save(commit=False)
        data.created_at = timezone.now()
        data.created_by = self.request.user.id
        data.user_name = self.request.user
        data.updated_at = timezone.now()
        data.save()

        # messages.add_message(self.request, messages.INFO, 'Document successfully saved')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('cabinet:list_proposals', kwargs={})

class ListProposal(ListView):
    model = ProposalCabinet
    template_name = 'cabinet/list_proposals.html'
    # clients = None
    def get_context_data(self, **kwargs):
        context = super(ListProposal, self).get_context_data(**kwargs)
        # clients = Client.objects.all().order_by('fullname_or_company_name')
        
        context['title'] = "Listing Proposals"
        # context['clients'] = clients
        return context

# # FBV HERE

# def search_document(request):
#     url = 'cabinet/list_documents.html'
#     if request.method == 'POST':
#         search_term = request.POST.get('search_no') 
#         cabinet = Cabinet.objects.filter(pk=search_term)
#     context = {
#         "object_list":cabinet,
#         'title':"Search Result for Document number "+search_term
#     }
#     return render(request, url, context)

# def document_filter(request):
   
#     # clients = Client.objects.all().order_by('fullname_or_company_name')
#     if request.method == 'POST':
       
#         # filter for document list
#         search_term = request.POST.get('search_term')
#         cabinet = request.POST.get('cabinet')
#         client_name = request.POST.get('client_name') 
#         client_type = request.POST.get('client_type') 
#         document_type =  request.POST.get('document_type')
#         function = request.POST.get('function')
#         name = None

#         filters = {}
       
#         if(search_term != ""):
      
#             filters['document_title__contains'] = search_term
          
#             # filters[','] = search_termx
#         if(function != ""):
#             filters['function'] = function
#         if(cabinet != ' '):
#             filters['cabinet'] = cabinet
#         if(client_type != "" and client_type != None ):
#             filters['client_type'] = client_type
#         if(document_type != ""):
#             filters['document_type'] = document_type
#         if(client_name != "" and client_name != None):
#             filters['client__id'] = client_name
  

#         documents = Cabinet.objects.filter(**filters )

#     else:
#         documents = Cabinet.objects.all().order_by('-id')
        

#     context = {
#         "object_list":documents,
#         "clients":clients,
#         'title':"Listing Filtered Documents"
#     }
#     return render(request, 'cabinet/list_documents.html', context)

class CreateProposal(CreateView):
    model = ProposalCabinet
    form_class = ProposalCreateForm
    template_name = 'cabinet/create_document.html'
    # success_url = '/list_documents'

    def form_valid(self, form): 
        data = form.save(commit=False)
        data.created_at = timezone.now()
        data.created_by = self.request.user.id
        data.user_name = self.request.user
        data.updated_at = timezone.now()
        data.save()

        # messages.add_message(self.request, messages.INFO, 'Document successfully saved')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('cabinet:list_proposals', kwargs={})

class ListProposals(ListView):
    model = ProposalCabinet
    template_name = 'cabinet/list_proposals.html'
    # clients = None
    def get_context_data(self, **kwargs):
        context = super(ListProposals, self).get_context_data(**kwargs)
        # clients = Client.objects.all().order_by('fullname_or_company_name')
        
        context['title'] = "Listing Proposals"
        # context['clients'] = clients
        return context
