from django.http import HttpResponse
from django.shortcuts import render

def index(request):
<<<<<<< HEAD
    return render(request,'home.html', {'name':'Navalny'})
=======
    return HttpResponse("Hello, world. You're at the polls index.")
>>>>>>> 49393aa0ff201196dcddf1d84202c0b5f587d2f4
