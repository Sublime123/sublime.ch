from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    return render(request,'home.html', {'name':'Navalny'})
    """
def add(request):
    val1 = request.POST['one']
    val2 = request.POST['two']
    res = str(int(val1) + int(val2))
    return render(request, 'result.html', {'result':res})
    """
def board(request):
    posts = []
    for post in Post.objects.all():
        #print (post.msg)
        posts.append(post.msg)
        """
    context = {
        "msg" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    """
    data = {'messages' : posts}
    return render(request, 'board.html', data)

def send(request):
    p = Post(title=request.POST["title"],\
        msg = request.POST["msg"])
    p.save()
    return render(request,'send.html')