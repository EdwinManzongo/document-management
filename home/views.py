from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required , permission_required
from .models import Authenticate 
from .forms import AuthenticateForm
from django.views.generic import (CreateView, DetailView, ListView, TemplateView, UpdateView)
from django.contrib.auth.models import Group


# Create your views here.
def home_logout(request):
    logout(request)
    return redirect('/')

def home_login(request):
    if request.method == "POST":

      user = authenticate(username=request.POST.get('username'), password = request.POST.get('password'))
      
      if(user is not None):
         login(request , user)
         # filter the Group model for current logged in user instance
         query_set = Group.objects.filter(user = request.user)
         
         # print to console for debug/checking
         for g in query_set:
            if g.name == "Student":
                return redirect('student/list_proposals')

         return redirect('cabinet/list_documents')
      else:
         messages.add_message(request, messages.ERROR, 'Invalid username or password')

    return render(request , "home/signin.html" , {}) 

class CreateAccount(CreateView):
    model = Authenticate
    form_class = AuthenticateForm
    template_name = 'home/create_account.html'
    # success_url = '/list_accounts'

    def form_valid(self, form): 
        data = form.save(commit=False)
        
        if Authenticate.objects.filter(username=data.username).exists():
            messages.add_message(self.request, messages.ERROR, 'User already exists.')
            return HttpResponseRedirect(self.get_error_url())
        else:
            data.save()
        return HttpResponseRedirect(self.get_success_url())
        
    def get_success_url(self):
        return reverse('home:list_accounts', kwargs={})

    def get_error_url(self):
        return reverse('home:create_account', kwargs={})

class ListAccounts(ListView):
    model = Authenticate
    template_name = 'home/list_accounts.html'

