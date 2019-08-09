from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, ProfileForm

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    user = request.user
    profile = Profile.objects.all()
    return render(request, 'homepage.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile})

def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    form = PostForm()
    commentForm = CommentForm()
    comments = Comment.objects.all()
    user = request.user
    profile = Profile.objects.all()
    profile_form = ProfileForm()
    return render(request, 'profile.html',{'form':form,'posts':posts,'commentForm':commentForm,'comments':comments, 'profile': profile, 'profile_form': profile_form})

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = ProfileForm()
        return render(request, 'profile.html')
    
    


def post_body(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('homepage')
    return redirect('homepage')

def post_comment(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('homepage')
    else:
        form = CommentForm()
        return redirect('homepage')
