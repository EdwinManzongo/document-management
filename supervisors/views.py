from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SupervisorCreateForm
from students.forms import StudentCreateForm
from .models import Supervisor 
from students.models import Student 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import date , datetime
from django.urls import reverse

from django.views.generic import (CreateView, DetailView, ListView, TemplateView, UpdateView)
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class CreateSupervisor(CreateView):
    model = Supervisor
    form_class = SupervisorCreateForm
    template_name = 'supervisors/create_supervisor.html'
    # success_url = '/list_supervisor'

    def form_valid(self, form): 
        data = form.save(commit=False)
        # print(data)
        data.supervisor_id = self.request.user
        data.created_at = timezone.now()
        data.created_by = self.request.user.id
        data.updated_at = timezone.now()
        data.save()

        # messages.add_message(self.request, messages.INFO, 'Supervisor successfully saved')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('supervisors:list_supervisor', kwargs={})

class ListSupervisors(ListView):
    model = Supervisor
    template_name = 'supervisors/list_supervisor.html'

class SupervisorsDetailView(DetailView):
    model = Supervisor
   
    template_name = "supervisors/view_supervisor.html"

class UpdateSupervisor(SuccessMessageMixin , UpdateView):
    model = Supervisor
    template_name = 'supervisors/update_supervisor.html'
    form_class = SupervisorCreateForm
    # success_message = 'Client successfully updated'

    # def get_context_data(self, **kwargs):
    #         context = super(Update_Client, self).get_context_data(**kwargs)
    #         context['title'] = "Updating information for Client no : "+str(self.kwargs['pk'])
    #         return context
            
    def get_success_url(self):
        return reverse('supervisors:list_supervisor', kwargs={})

# class DeleteClient(DeleteView):
#     model = Client
#     success_url = '/clients/list_clients'
#     success_message = "Client deleted successfully."
#     def delete(self, request, *args, **kwargs):
#         messages.add_message(self.request, messages.INFO , self.success_message)
#         return super(DeleteClient, self).delete(request, *args, **kwargs)
    
class ListStudents(ListView):
    model = Student
    template_name = 'supervisors/list_profile.html'

class StudentsDetailView(DetailView):
    model = Student
   
    template_name = "supervisors/view_profile.html"

class UpdateStudent(SuccessMessageMixin , UpdateView):
    model = Student
    template_name = 'supervisors/update_profile.html'
    form_class = StudentCreateForm
            
    def get_success_url(self):
        pk = self.request.user.id
        return reverse('supervisors:view_profile', kwargs={"pk": pk})