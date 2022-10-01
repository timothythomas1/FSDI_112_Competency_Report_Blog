from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]

# delete view for details
class PostDeleteView(DeleteView):
    # specify the model you want to use
    model = Post
    # can specify success url
    # url to redirect after successfully
    success_url ="/posts"
    # deleting object
    template_name = "posts/confirm_delete.html"
