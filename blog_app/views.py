from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.

# Post
def create_post(request):
    form = PostForm
    message = None
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            get_post_name = form.cleaned_data.get('title')
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            message = f'The post {get_post_name} was created successfully'
    context = {
        'post_form':form,
        'success_message':message
    }
    return render(request, 'post.html', context)

# GET
def view_posts(request):
    get_post = Post.objects.all()
    context = {
        "post": get_post
    }
    return render(request, 'users_post.html', context)

# Delete
def delete_post(request, id):
    query_post = Post.objects.get(id=id)
    query_post.delete()
    return redirect('posts')