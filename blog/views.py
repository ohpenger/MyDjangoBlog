from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
import markdown
import pygments
from comments.forms import CommentForm
from comments.models import Comments
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
# Create your views here.
def index(request):
    post_list=Post.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})
def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.increase_views()
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    form=CommentForm()
    comment_list=Comments.objects.filter(post=pk)
    context={'post':post,
             'form':form,
             'comment_list':comment_list
    }
    return render(request,'blog/detail.html',context=context)
def archives(request,year,month):
    post_list=Post.objects.filter(created_time__year=year,created_time__month=month)
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})
def catagory(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate)
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})
def tag(request,pk):
    atag=get_object_or_404(Tag,pk=pk)
    post_list=atag.post_set.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})