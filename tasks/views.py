from django.shortcuts import render

tasks = ["check emails", "send email", "set meets"]

# Create your views here.
def index(request):
    return render(request, "index.html", {"tasks": tasks})


def add(request):
    return render(request, "add.html")
