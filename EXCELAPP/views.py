from django.shortcuts import render,redirect
from .resources import IPLresources
from django.contrib import messages
from tablib import Dataset
from .models import *
from django.http import HttpResponse




def index(request):
    if request.method =='POST':
        IPL_resource = IPLresources()
        dataset = Dataset()
        new_ipl_resource = request.FILES['myfiles']
        imported_data = dataset.load(new_ipl_resource.read(),format='xlsx')
        

        if not new_ipl_resource.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render (request, 'index.html')
        # elif len(imported_data) > 17:
        #     messages.info(request,"Files Column doesn't match Database Column! Kindly Check Selected File Column again")
        #     return redirect('/')
        # imported_data = dataset.load(new_ipl_resource.read(),format='xlsx')
        else:
           for data in imported_data:
                   value = IPL(
                   data[0],
                   data[1],
                   data[2],
                   data[3],
                   data[4],
                   data[5],
                   data[6],
                   data[7],
                   data[8],
                   data[9],
                   data[10],
                   data[11],
                   data[12],
                   data[13],
                   data[14],
                   data[15],
                   data[16],
               )
                
                   value.save()
                   print(len(imported_data))
    return render (request, 'index.html')