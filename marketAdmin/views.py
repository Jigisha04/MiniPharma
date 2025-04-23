from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import medicines, health
from django.utils.decorators import method_decorator
from MiniMarket.middleware import checkUserStatus
# Create your views here.


# grocery wala hai
# @method_decorator(checkUserStatus)

class healthList(ListView):
  
    model = health
    
    template_name = 'marketAdmin/health.html'
    context_object_name = 'health'
    ordering = ['id']
    paginate_by = 7



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] =  self.request.userdata
        return context

   





#   sabji wala hai   
class medicinesList(ListView):
    model = medicines
    template_name = 'marketAdmin/medicines.html'
    context_object_name = 'medicines'
    ordering = ['id']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userdata"] =  self.request.userdata
        return context
  