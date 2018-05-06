from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'polls/header.html')

def cv(request):
    return render(request, 'polls/cv.html')
