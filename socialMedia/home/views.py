from django.shortcuts import render, redirect
from django.views import View
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
class HomeView(View):
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, 'home/index.html',{'posts':posts})
    def post(self, request):
        posts = Posts.objects.all()
        return render(request, 'home/index.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Posts.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'home/detail.html', {'post': post})


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Posts.objects.get(pk=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'your post deleted successfully', 'success')
            return redirect('home:home')
        else:
            messages.error(request, 'you are not allowed to delete this post', 'danger')
            return redirect(request, 'home:home')
