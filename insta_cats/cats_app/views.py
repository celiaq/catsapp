from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CatPostForm
from .models import CatPost


def index(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_post')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create_post')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CatPostForm(request.POST, request.FILES)
        if form.is_valid():
            cat_post = form.save(commit=False)
            cat_post.user = request.user
            cat_post.save() 
            return redirect('index')
    else:
        form = CatPostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'create_post.html', context)

def view_photos(request):
    cat_posts = CatPost.objects.all()
    
    context = {
        'cat_posts': cat_posts,
    }
    return render(request, 'view_photos.html', context)

def delete_photo(request, post_pk):
    post = get_object_or_404(CatPost, pk=post_pk)
    
    if request.method == 'POST':
        post.delete()
    return redirect('view_photos')