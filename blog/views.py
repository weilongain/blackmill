from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html', )


def blogPost(request,pk):
    try:
        queryset = models.Post.objects.get(id=pk)
        if queryset.publish == True:
            context = {"queryset":queryset}
            return render(request,"post.html",context)
        else:
            return render(request, 'index.html',)
    except:
        return render(request, 'index.html',)


def about(request):
    return render(request,"about.html")
