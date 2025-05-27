from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def helloEveryone(request):
    return HttpResponse("Hello World!")


def helloUser(request, name):
    return render(request, "hello/helloUser.html", {"name": name.capitalize()})


def userData(request):
    data = {
        "users": [
            {
                "name": "Taha",
                "age": 25,
                "native_language": "Turkish",
                "second_language": "English",
            },
            {
                "name": "Aslı",
                "age": 18,
                "native_language": "Turkish",
                "second_language": "English",
            },
            {
                "name": "Ahmet",
                "age": 30,
                "native_language": "Turkish",
                "second_language": "English",
            },
            {
                "name": "Ayşe",
                "age": 22,
                "native_language": "Turkish",
                "second_language": "English",
            },
        ]
    }
    return render(request, "hello/greet.html", data)
