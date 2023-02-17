from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return render(request, 'members.html')
# Create your views here.
