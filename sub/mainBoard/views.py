from cgitb import text
from threading import Thread
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from .models import Threads
from django.http import HttpResponseRedirect
from .forms import PostForm
from .forms import ThreadForm
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser
from math import floor
def index(request):
    return render(request,'home.html')

def getMessagesForScreen(listOfAll,screen,postsPerScreen):
    result = []
    for idx,val in enumerate(listOfAll):
        if idx >= screen * postsPerScreen and idx < (screen + 1) * postsPerScreen:
            result.append(val)
    screenMax = floor(len(listOfAll) / postsPerScreen)
    return screenMax,result


def board(request):
    """
    form = PostForm()
    posts_per_screen = 50
    listOfAll = list(Post.objects.order_by('-number'))
    screen = request.GET.get("screen", 0)
    messages = getMessagesForScreen(listOfAll,screen,posts_per_screen)
    posts = []
    for post in Post.objects.all():
        #print (post.msg)
        posts.append(post.msg)        
    data = {'messages' : posts}
    return render(request, 'board.html', data)
    """
    th = []
    threads = list(Threads.objects.order_by('bump'))
    posts_per_screen = 2
    try:
        screen = int(request.GET.get("screen", 0))
    except:
        screen = 0
    maxScreen, threads = getMessagesForScreen(threads,screen,posts_per_screen)
    for thread in threads:    
        oppost = list(Post.objects.filter(thread=thread).filter(opPost=True))
        posts = list(Post.objects.filter(thread=thread).filter(opPost=False).order_by('-number'))
        th.append({'op':oppost[0], 'posts':posts})
    screens = []
    for n in range(maxScreen + 1):
        screens.append({'screen':n, 'current': True if n == screen else False})
    print(screens)
    data = {'threads':th,'screens':screens}

    return render(request, 'board.html', data)

def thread(request):
    form = ThreadForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user if request.user.is_anonymous == False else None
        post.published_date = timezone.now()
        post.pic = request.FILES.get('pic')
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def send(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user if request.user.is_anonymous == False else None
        post.published_date = timezone.now()
        post.pic = request.FILES.get('pic')
        post.save()
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
