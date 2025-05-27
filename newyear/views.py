from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {"now": now})
