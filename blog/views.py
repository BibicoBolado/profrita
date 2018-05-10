from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Post
# Create your views here.
def index(request):
    postagens=Post.objects.order_by('-created_date').all()
    paginator=Paginator(postagens,6)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context={}
    context['posts']=posts
    template_name='blog/index.html'
    return render(request,template_name,context)

def home(request):
    template_name='blog/home.html'
    return render(request,template_name)

def post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    template_name='blog/post.html'
    context={'post':post}
    return render(request,template_name,context)

def contato(request):
    template_name='blog/contato.html'
    return render(request,template_name)