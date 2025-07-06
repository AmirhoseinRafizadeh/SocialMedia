from django.shortcuts import render, redirect
from django.views import View
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostUpdateForm
from django.utils.text import slugify


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

class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostUpdateForm
    def setup(self, request, *args, **kwargs):
        self.post_instace = Posts.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    def dispatch(self, request, *args, **kwargs):
        post = self.post_instace
        if post.user.id != request.user.id:
            messages.error(request, 'you are not allowed to edit someone else posts', 'danger')
            return redirect(request, 'home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        post = self.post_instace
        form = self.form_class(instance=post)
        return render(request, 'home/update.html', {'form': form})
    def post(self, request, *args, **kwargs):
        post = self.post_instace
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(request, 'your post updated successfully', 'success')
            return redirect('home:post_detail', post.id, post.slug)
