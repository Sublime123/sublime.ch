from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.utils import timezone

def index(request):
    return render(request,'home.html')

def board(request):
    form = PostForm()
    messages = []
    messages = list(Post.objects.order_by('number')[:50])
    return render(request, 'board.html', {'form': form,'messages':messages})
    """
    posts = []
    for post in Post.objects.all():
        #print (post.msg)
        posts.append(post.msg)        
    data = {'messages' : posts}
    return render(request, 'board.html', data)
"""


def send(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.published_date = timezone.now()
        post.save()
        print(post)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    """
    if request.method == 'POST':
        p = Post(title=request.POST["title"],\
            msg = request.POST["msg"])
        p.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,'send.html')

    from .forms import NameForm
    """
