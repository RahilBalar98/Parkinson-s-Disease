from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
from parkinson.settings import MEDIA_ROOT
import pickle

def index(request):
    response = render(request, 'pd/index.html', {})
    return response

def getData(request):
     if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        n = request.POST.get('number')
        # no = int(n)
        print(n)
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        
        print(filename)
        # upload_file = "/home/shail/Documents/parkinson/website/django-apps/parkinson/"+myfile
        data = pd.read_csv(MEDIA_ROOT + filename)
        print(data)
        modelName="/home/shail/Documents/parkinson/website/django-apps/parkinson/pd/voice_model.sav"
        # Load the pickled model 
        model_from_pickle = pickle.load(open(modelName, 'rb'))
        # Use the loaded pickled model to make predictions 
        finalData = model_from_pickle.predict(data)

        print(finalData)
        if(finalData[10]==1):
            answer = "Parkinsonian positive"
        else:
            answer = "Parkinsonian negative"


        return JsonResponse({"url": answer})

def getDataTremor(request):
    print(request.POST)
    if request.method == 'POST' and request.FILES['file'] and request.POST.get('numberT'):
        myfile = request.FILES['file']
        n = request.POST.get('numberT')
        no = int(n)
        print(n)
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        
        print(filename)
        # upload_file = "/home/shail/Documents/parkinson/website/django-apps/parkinson/"+myfile
        data = pd.read_csv(MEDIA_ROOT + filename)
        print(type(data))
        # d = [data[0]]
        modelName="/home/shail/Documents/parkinson/website/django-apps/parkinson/pd/tremor_model.sav"
        # Load the pickled model 
        model_from_pickle = pickle.load(open(modelName, 'rb'))
        # Use the loaded pickled model to make predictions 
        finalData = model_from_pickle.predict(data)

        print(finalData)
        if(finalData[no]==1):
            answer = "Parkinsonian positive"
        else:
            answer = "Parkinsonian negative"


        return JsonResponse({"url": answer})
    return JsonResponse({"url": "error"})

def getDataBrady(request):
     if request.method == 'POST' and request.FILES['file'] and request.POST.get('numberB'):
        myfile = request.FILES['file']
        n = request.POST.get('numberB')
        no = int(n)
        print(no)
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        
        print(filename)
        # upload_file = "/home/shail/Documents/parkinson/website/django-apps/parkinson/"+myfile
        data = pd.read_csv(MEDIA_ROOT + filename)
        print(data)
        modelName="/home/shail/Documents/parkinson/website/django-apps/parkinson/pd/tappy_model.sav"
        # Load the pickled model 
        model_from_pickle = pickle.load(open(modelName, 'rb'))
        # Use the loaded pickled model to make predictions 
        finalData = model_from_pickle.predict(data)

        print(finalData)
        if(finalData[no]==1):
            answer = "Parkinsonian positive"
        else:
            answer = "Parkinsonian negative"


        return JsonResponse({"url": answer})

def getDataGait(request):
     if request.method == 'POST' and request.FILES['file'] and request.POST.get('numberG'):
        myfile = request.FILES['file']
        n = request.POST.get('numberG')
        no = int(n)
        print(n)
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        
        print(filename)
        # upload_file = "/home/shail/Documents/parkinson/website/django-apps/parkinson/"+myfile
        data = pd.read_csv(MEDIA_ROOT + filename)
        print(data)
        modelName="/home/shail/Documents/parkinson/website/django-apps/parkinson/pd/gait_model.sav"
        # Load the pickled model 
        model_from_pickle = pickle.load(open(modelName, 'rb'))
        # Use the loaded pickled model to make predictions 
        finalData = model_from_pickle.predict(data)

        print(finalData)
        if(finalData[no]==1):
            answer = "Parkinsonian positive"
        else:
            answer = "Parkinsonian negative"


        return JsonResponse({"url": answer})