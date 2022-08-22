from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.utils import timezone

from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    return render(
        request,
        "blog/post_list.html",
        {"posts": posts},
    )


def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return HttpResponseRedirect("/")
    else:
        form = PostForm()
        return render(
            request,
            "blog/post_create.html",
            {"form": form},
        )

@login_required
def post_draft_list(request):
    drafts = Post.objects.filter(published_date__isnull=True).order_by("created_date")
    return render(
        request,
        "blog/post_draft_list.html",
        {"drafts": drafts},
    )
@login_required    
def post_publish(request,pk):
        post = get_object_or_404(post, pk=pk)
        post.published_date = timezone.now()
        post.save()
        return HttpResponseRedirect("/")
@login_required
def post_delete(request,pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return HttpResponseRedirect("/")


@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect("/post-draft-list/")
    else:
        form = PostForm(instance=post)
        return render(
            request,
            "blog/post_create.html",
            {"form": form},
        )

#def post_edit(request,pk):
    #if request.method == "POST":
        #form = PostForm(request.POST, instance=post)
        #if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.save()
            #return HttpResponseRedirect("/")
    #else:
        #form = PostForm(instance=post)
        #return render(
            #request,
            #"blog/post_create.html",
            #{"form": form, "post":post},
        #)