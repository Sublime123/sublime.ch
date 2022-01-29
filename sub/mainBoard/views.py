from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home.html', {'name':'Navalny'})
def add(request):
    val1 = request.POST['one']
    val2 = request.POST['two']
    res = str(int(val1) + int(val2))
    return render(request, 'result.html', {'result':res})