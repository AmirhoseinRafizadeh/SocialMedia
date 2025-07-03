from django.shortcuts import render
from django.views import View
from .models import Posts


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


