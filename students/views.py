from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StudentCreateForm
from .models import Student 
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
        return reverse('students:list_profile', kwargs={})

class ListStudents(ListView):
    model = Student
    template_name = 'students/list_profile.html'

class StudentsDetailView(DetailView):
    model = Student
   
    template_name = "students/view_profile.html"

class Update_Student(SuccessMessageMixin , UpdateView):
    model = Student
    template_name = 'students/update_profile.html'
    form_class = StudentCreateForm
    # success_message = 'Client successfully updated'

    # def get_context_data(self, **kwargs):
    #         context = super(Update_Client, self).get_context_data(**kwargs)
    #         context['title'] = "Updating information for Client no : "+str(self.kwargs['pk'])
    #         return context
            
    def get_success_url(self):
        return reverse('student:list_profile', kwargs={})

# class DeleteClient(DeleteView):
#     model = Client
#     success_url = '/clients/list_clients'
#     success_message = "Client deleted successfully."
#     def delete(self, request, *args, **kwargs):
#         messages.add_message(self.request, messages.INFO , self.success_message)
#         return super(DeleteClient, self).delete(request, *args, **kwargs)
    