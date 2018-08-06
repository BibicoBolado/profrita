from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .forms import Contact

from .models import Post
# Create your views here.

def index(request):
    postagens = Post.query_posts(Post)
    #Com o cod acima posso escrever 
    #minhas querys dentro do  model
    #e somente chamas de dentro  da
    #view, deixando   elas  menores

    ###########Paginação############
    paginator=Paginator(postagens,6)
    page = request.GET.get('page')
    print(page)
    print(dir(paginator))
    posts = paginator.get_page(page)
    ################################
    context={}
    context['posts']=posts
    template_name='blog/index.html'
    return render(request,template_name,context)

def home(request):
    template_name='blog/home.html'
    return render(request,template_name)

def post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    print(post.numReads)
    post.addNumRead()
    time_read=post.time_read()
    print("%f: %s" %(time_read,"minutos"))
    print(post.query_posts())
    template_name='blog/post.html'
    context={'post':post,'time_read':time_read}
    return render(request,template_name,context)

def contato(request):
    template_name='blog/contato.html'
    context = {}
    if request.method=='POST':
        form = Contact(request.POST)
        if form.is_valid():
            context['is_valid']=True
            print(form.cleaned_data)
            form.sendMail(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['message'])
            #só posso usar depois do is_valid
            form= Contact()
    else:
        form = Contact()
    context['form']=form
    return render(request,template_name,context)