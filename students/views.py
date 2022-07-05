from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StudentCreateForm, DocumentCreateForm, DocumentEditForm
from .models import Student 
from cabinet.models import Cabinet, ProposalCabinet
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import date , datetime
from django.urls import reverse

from django.views.generic import (CreateView, DetailView, ListView, TemplateView, UpdateView)
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class CreateStudent(CreateView):
    model = Student
    form_class = StudentCreateForm
    template_name = 'students/create_profile.html'
    # success_url = '/list_profile'

    def form_valid(self, form): 
        data = form.save(commit=False)
        # print(data)
        data.student_id = self.request.user
        data.created_at = timezone.now()
        data.created_by = self.request.user.id
        data.user_id = self.request.user.username
        data.updated_at = timezone.now()
        data.save()

        # messages.add_message(self.request, messages.INFO, 'Student successfully saved')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # pk = self.request.user.id
        # return reverse('students:view_profile', kwargs={"pk": pk})
        return reverse('students:list_documents', kwargs={})

class ListStudents(ListView):
    model = Student
    template_name = 'students/list_profile.html'

def student_dashboard(request):
    all_calls = Cabinet.objects.filter(user_name = request.user)

    context = {
        'title':'Your Documents',
        'all_calls': all_calls,
    }

    return render(request , "students/list_documents.html" , context) 

def student_trail(request):
    all_calls = Cabinet.objects.filter(user_name = request.user)

    context = {
        'title':'Documents Trail',
        'all_calls': all_calls,
    }

    return render(request , "students/documents_trail.html" , context) 

class StudentsDetailView(DetailView):
    model = Student
   
    template_name = "students/view_profile.html"

class UpdateStudent(SuccessMessageMixin , UpdateView):
    model = Student
    template_name = 'students/update_profile.html'
    form_class = StudentCreateForm
            
    def get_success_url(self):
        pk = self.request.user.id
        return reverse('students:view_profile', kwargs={"pk": pk})

class DeleteStudent(DeleteView):
    model = Student
    success_url = '/student/list_profile'
    # success_message = "Student deleted successfully."
    def delete(self, request, *args, **kwargs):
        # messages.add_message(self.request, messages.INFO , self.success_message)
        return super(DeleteStudent, self).delete(request, *args, **kwargs)

# Create Document Views
class CreateDocument(CreateView):
    model = Cabinet
    form_class = DocumentCreateForm
    template_name = 'students/create_document.html'
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
        return reverse('student:list_documents', kwargs={})

class UpdateDocument(SuccessMessageMixin, UpdateView):
    model = Cabinet
    template_name = 'students/update_document.html'
    form_class = DocumentEditForm
    # success_message = 'Document  updated'

    def get_context_data(self, **kwargs):
            context = super(UpdateDocument, self).get_context_data(**kwargs)
            context['title'] = "Updating information for Document no : "+str(self.kwargs['pk'])
            return context
            
    def get_success_url(self):
        return reverse('student:list_documents', kwargs={})

class DocumentDetailView(DetailView):
    model = Cabinet
   
    template_name = "students/view_document.html"

class ListDocuments(ListView):
    model = Cabinet
    template_name = 'students/list_documents.html'
    # clients = None
    def get_context_data(self, **kwargs):
        context = super(ListDocuments, self).get_context_data(**kwargs)
        # clients = Client.objects.all().order_by('fullname_or_company_name')
        
        context['title'] = "Listing Documents"
        # context['clients'] = clients
        return context
    
class ListProposal(ListView):
    model = ProposalCabinet
    template_name = 'students/list_proposals.html'
    # clients = None
    def get_context_data(self, **kwargs):
        context = super(ListProposal, self).get_context_data(**kwargs)
        # clients = Client.objects.all().order_by('fullname_or_company_name')
        
        context['title'] = "Listing Proposals"
        # context['clients'] = clients
        return context