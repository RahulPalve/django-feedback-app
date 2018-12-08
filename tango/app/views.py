from django.shortcuts import render
from django.http import HttpResponse
from app.models import Post


posts=Post.objects.all()


def index(request):
    return render(request,"app.html",{'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)				
    return render(request,'post_detail.html',{'post':post})


# Create your views here.
