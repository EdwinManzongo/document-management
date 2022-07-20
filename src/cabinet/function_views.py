from django.http import HttpResponseRedirect , JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from django.core import serializers

from django.utils import timezone
from datetime import date , datetime
import json



from django.db.models import Q
from django.http import HttpResponse



# Function Based Views 
# def patient_data(request):

#     form = None
#     diag_form = None
#     comb_data = []
   
#     if request.method == 'POST':
#         form = Patient_Data_Form(request.POST )

#         if form.is_valid():
            
#             pass
#     elif request.is_ajax():
#         sublclass = {}
#         subclass = list(Patients.objects.filter(pk=request.GET.get('class', None)).values())
#         appointment = list(Appointment.objects.filter(patient_id__id=request.GET.get('class', None)).values())
        
#         # comb_data[0] = subclass
#         # comb_data[1] = appointment
#         subclass.append(appointment)

#         # print(subclass[1])
   
       
#         return JsonResponse(subclass , safe=False)
#     else:
#         diag_form = DiagnosisCreateForm()
#         pass
#         #form = Patient_Data_Form()
#         # form = Patient_Data_Form(initial={'patient':request.user.patient})  
#     context = {
#         'form': form,
#         'diag_form': diag_form,
#         'title': "Patient Data" ,
#     }

#     return render(request, 'patient/org_patient_data.html', context)

def function_data(request):

    episode = []
    if request.is_ajax():
        cabinets = ()
        function_name = request.GET.get('function_name', None) 
      

        if(function_name == 'underwriting'):

            cabinets = (
            (" ", '----Select Underwriting Cabinet-----'),
            ('General File' , 'General File'),
            ('Motor File' ,'Motor File'),
            ('Assets All Risks' ,'Assets All Risks'),
            ('Electronic Equipment' ,'Electronic Equipment'),
            ('Machinery Breakdown' ,'Machinery Breakdown'),
            ('Deterioration of stock' ,'Deterioration of stock'),
            ('Loan Protection', 'Loan Protection'),
            ('Public Liability Policy', 'Public Liability Policy'),
            ('Umbrella Liability Policy', 'Umbrella Liability Policy'),
            ('Employers Liability Policy', 'Employers Liability Policy'),
            ('Products Liability Policy', 'Products Liability Policy'),
            ('Plant All Risks Policy', 'Plant All Risks Policy'),
            ('Carriers Liability Policy', 'Carriers Liability Policy'),
            ('Warehouseman Liability', 'Warehouseman Liability'),
            ('Directors and Officers Liability', 'Directors and Officers Liability'),
            ('Plant All Risks', 'Plant All Risks'),
            ('Tobacco Stock throughput', 'Tobacco Stock throughput'),
            ('Marine Hull', 'Marine Hull'),
            ('Open Marine Cargo', 'Open Marine Cargo'),
            ('Fidelity Guarantee Policy', 'Fidelity Guarantee Policy'),
            ('Credit Insurance', 'Credit Insurance'),
            ('Home Combined Policy', 'Home Combined Policy'),
            ('Group Personal Accident', 'Group Personal Accident'),
            ('Directors Personal Accident', 'Directors Personal Accident'),
            ('Professional Indemnity', 'Professional Indemnity'),
            ('Advance payment guarantee', 'Advance payment guarantee'),
            ('Bid Bond', 'Bid Bond'),
            ('Performance Bond', 'Performance Bond'),
            ('Farm Comprehensive Policy', 'Farm Comprehensive Policy'),
            ('Goods in Transit Policy', 'Goods in Transit Policy'),
            ('Open Marine Policy', 'Open Marine Policy'),
            ('Contractors All Risks', 'Contractors All Risks'),
            ('Erection All Risks', 'Erection All Risks'),

            ('', '----Individual Cabinet-----'),
            ('Motor', 'Motor'),
            ('Houseowners','Houseowners'),
            )
          
        elif(function_name == 'claims'):
     
            cabinets = (
                (" ", '----Select Claims Cabinet-----'),
                ('Assets','Asset'), 
                ('Motor','Motor'),
                ('Group Personal Accident (GPA)','Group Personal Accident (GPA)'),
                ('Electronic Equipment','Electronic Equipment'),
                ('Public Liability','Public Liability'),
                ('Fidelity Guarantee (FG)','Fidelity Guarantee (FG)'),
                ('Loan Protection','Loan Protection'),
                ('Home Combined','Home Combined'),
                ('Machinery Breakdown','Machinery Breakdown'),
                ('Deterioration of Stock','Deterioration of Stock'),
                ('Agriculture (Crop & Livestock)','Agriculture (Crop & Livestock)'),
                ('Miscellaneous','Miscellaneous'),
               
            )
        else:
            pass

  
   
        episode.insert(0 , cabinets)

  

     
    context = {
      
    }
    return JsonResponse(episode , safe=False)

