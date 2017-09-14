from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import UploadFileForm

import pandas

# Create your views here.

#def index(request):
#    context = {
#        'name': 'Undefined Curiosity',
#        }    
#
#    return render(request, 'prototype/index.html', context)





def handle_uploaded_file(f):
    doc = pandas.read_csv(f).head(10).to_html()
    return doc

    #doc = []
    #for chunk in f.chunks():
    #    doc.append(chunk)
    #return doc

    #with open('some/file/name.txt', 'wb+') as destination:
    #    for chunk in f.chunks():
    #        destination.write(chunk)


def index(request):
    uploaded_data = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_data = handle_uploaded_file(request.FILES['file'])
            #print(uploaded_data)
            #return HttpResponseRedirect('/data/')
    else:
        form = UploadFileForm()
        
    context = {
        'form': form
        ,'uploaded_data':uploaded_data
        ,'name':'Undefined Curiosity'
        }    

    return render(request, 'prototype/index.html', {'form': form, 'uploaded_data':uploaded_data})

