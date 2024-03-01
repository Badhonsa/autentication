import os

from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Talk(request):
    return render(request, "Accounts/GREAT.html")
