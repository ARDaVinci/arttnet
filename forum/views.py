from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView,)
from .models import Post , Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_object_or_404 , render, redirect
from .forms import PostForm , CommentForm
from django.utils.text import slugify
from django.http import Http404

# Create your views here.
class PostList( LoginRequiredMixin , ListView):
    login_url = '/intranet_artt/login/'
    template_name = 'forum/posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-creation_date')

class PostDetail(LoginRequiredMixin , DetailView):
    login_url = '/intranet_artt/login/'
    template_name = 'forum/post.html'
    model = Post


class PostCreate( LoginRequiredMixin , CreateView ):
    login_url = '/intranet_artt/login/'
    model = Post
    fields = [ 'title' , 'text']

    def form_valid(self, form):
        self.object = form.save(commit= False)
        self.object.sender =self.request.user
        self.object.creation_date = datetime.datetime.now()
        self.object.save()
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin  , UpdateView):
    login_url = '/intranet_artt/login/'
    model = Post
    fields =  [ 'title' , 'text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.sender == self.request.user:
            self.object.save()
            return super().form_valid(form)
        else:
            raise Http404("Vous n'êtes pas autorisé(e) à modifier ce post")


class PostDelete(LoginRequiredMixin  , DeleteView):
    login_url = '/intranet_artt/login/'
    model = Post

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.username == self.object.sender.username:
            self.object.delete()
            return redirect("posts:posts")
        else:
            raise Http404("Vous n'êtes pas autorisé(e) à supprimer ce post")



@login_required
def add_comment(request , pk):
    post = get_object_or_404(Post , pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            post.total_comments = post.total_comments + 1
            post.save()
            comment.comment_id = post.total_comments
            comment.author = request.user
            comment.creation_date = datetime.datetime.now()
            comment.slug = slugify(comment.comment_id)
            comment.save()

            return redirect('posts:post' , pk=post.pk)

    else:
        form = CommentForm()

    return render(request, 'forum/comment_form.html' , {'form':form})


@login_required
def update_comment(request , pk , slug):
    post = get_object_or_404(Post , pk=pk)
    comment = get_object_or_404(Comment ,post=post , slug=slug)

    if comment.author.username == request.user.username:

        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)

            if form.is_valid():
                form.save()

                return redirect('posts:post' , pk=post.pk)

        else:
                form = CommentForm()


        return render(request, 'forum/comment_form.html' , {'form':form})

    else:
        raise Http404("Vous n'êtes pas autorisé(e) à modifier ce commentaire")


@login_required
def delete_comment(request , pk , slug):
    post = get_object_or_404(Post , pk=pk)
    comment = get_object_or_404(Comment , post=post , slug=slug)
    if request.user.username == comment.author.username:
        comment.delete()
        return redirect('posts:post' , pk=post.pk)
    else:
        raise Http404("Vous n'êtes pas autorisé(e) à supprimer ce commentaire")


