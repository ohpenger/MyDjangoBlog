from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comments
from .forms import CommentForm


# Create your views here.
def post_comment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comments=form.save(commit=False)
            comments.post=post
            comments.save()
            return redirect(post)
        else:
            comment_list=post.comments_set.all()
            context={'post':post,
                     'form':form,
                     'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
