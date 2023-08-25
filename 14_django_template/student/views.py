from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('<h1>HELLO</h1>')

    context = {
        "title": "cosmios",
        "description": "This is description",
        "number": 112,
        "list1": ["a","b",1,[1,2]],
        "dict1": {
            "a":1,  
            "b":2
        }
    }
    return render(request, 'student/home.html', context)


def product(request):
    return render(request, 'student/products.html')


# {{ veriable }} 
# {% comand %}
# | ---------> filitreleme