from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage

from .forms import DocumentForm
from .models import Document

import pandas


##################################################
# Manipulation Functions
#   This section will be functions that will allow
#   us to manipulate data. Consider where we'll
#   maintain this. Some special class?
##################################################

def handle_uploaded_file(f):
    '''Handle Upload File
        Function to transform csv file to HTML table
    '''
    doc = pandas.read_csv(f).head(10).to_html()
    return doc

    #with open('some/file/name.txt', 'wb+') as destination:
    #    for chunk in f.chunks():
    #        destination.write(chunk)

##################################################
#   End manipulation functions
##################################################


def index(request):
    '''Index Page
        Web page view to enable uploading
        capabilities
    '''

    documents = Document.objects.all()
    uploaded_file_url = None
    uploaded_data = None
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_data = handle_uploaded_file(request.FILES['document'])
            form.save()
    else:
        form = DocumentForm()
        
    context = {
        'form': form
        ,'uploaded_data':uploaded_data
        ,'documents': documents
        ,'name':'Undefined Curiosity'
        
        }    

    return render(request, 'prototype/index.html', context)

