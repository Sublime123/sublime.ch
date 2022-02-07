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
from math import floor, ceil
from django.http import HttpResponseNotFound
from django.db.models import Max

def index(request):
    return render(request,'home.html')

def getMessagesForScreen(listOfAll,screen,postsPerScreen):
    result = []
    for idx,val in enumerate(listOfAll):
        if idx >= screen * postsPerScreen and idx < (screen + 1) * postsPerScreen:
            result.append(val)
    screenMax = ceil(len(listOfAll) / postsPerScreen)
    return screenMax,result


def board(request):
    if request.method =='POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user if request.user.is_anonymous == False else None
            post.published_date = timezone.now()
            post.pic = request.FILES.get('pic')
            post.opPost = True
            thread = Threads()
            #
            #thread = Threads.objects.all().filter(threadNumber=threadId)
            bumpCounter = Threads.objects.aggregate(Max('bump'))
            if bumpCounter['bump__max'] is not None:
                bumpCounter = bumpCounter['bump__max'] + 1
            else:
                bumpCounter = 0
            thread.bump = bumpCounter
            thread.save()
            #            
            post.thread = thread            
            post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    elif request.method =='GET':
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
        threads = list(Threads.objects.order_by('-bump'))
        posts_per_screen = 10
        try:
            screen = int(request.GET.get("screen", 0))
        except:
            screen = 0
        maxScreen, threads = getMessagesForScreen(threads,screen,posts_per_screen)
        for thread in threads:
            oppost = list(Post.objects.filter(thread=thread).filter(opPost=True))
            posts = list(Post.objects.filter(thread=thread).filter(opPost=False).order_by('number'))
            posts = posts[len(posts) - 5:len(posts)]
            if len(oppost) > 0:
                th.append({'op':oppost[0], 'op_link':'thread?t=' + str(oppost[0].thread.threadNumber), 'posts':posts})
        screens = []
        for n in range(maxScreen):
            screens.append({'screen':n, 'current': True if n == screen else False})
        form = ThreadForm()
        data = {'threads':th,'screens':screens, 'form':form}

        return render(request, 'board.html', data)

def thread(request):
    if request.method =='POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user if request.user.is_anonymous == False else None
            post.published_date = timezone.now()
            post.pic = request.FILES.get('pic')
            post.opPost = False
            threadId=request.POST.get('threadId')
            thread = Threads.objects.all().filter(threadNumber=threadId)
            bump = thread.aggregate(Max('bump'))
            bump = bump['bump__max'] + 1
            thread.update(bump=bump)
            post.thread = list(thread)[0]
            post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    elif request.method =='GET':
        threadId = int(request.GET.get("t", 0))
        form = PostForm()
        if threadId > 0:
            oppost = list(Post.objects.filter(thread=threadId).filter(opPost=True))
            posts = list(Post.objects.filter(thread=threadId).filter(opPost=False).order_by('number'))
            data = {'oppost':oppost[0], 'posts':posts, 'threadId':threadId,'form':form}
            return render(request, 'thread.html', data)
        return HttpResponseNotFound("<h1>404</h1>")         

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
