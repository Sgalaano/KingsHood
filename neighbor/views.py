from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

# Create your views here.
# @login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    posts = Post.objects.filter(neighborhood = profile.neighborhood)
    businesses = Business.objects.filter(neighborhood = profile.neighborhood)
    hood = profile.neighborhood
    return render(request,'index.html', locals())


# @login_required(login_url='/accounts/login')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        profile = Profile.objects.get(user = request.user)
        search_term = request.GET.get('search')
        results = Business.objects.filter(neighborhood = profile.neighborhood, name__icontains = search_term)
        message = f'{search_term}'
    return render(request, 'search.html', locals())

# @login_required(login_url='/accounts/login')
def business(request):
    profile = Profile.objects.get(user = request.user)
    businesses = Business.objects.filter(neighborhood = profile.neighborhood)
    return render(request, 'business.html', locals())

# @login_required(login_url='/accounts/login')
def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post = post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('post', id)
    else:
        form = CommentForm()
    return render(request, 'post.html', locals())

# @login_required(login_url='/accounts/login')
def profile(request, id):
    disp_user = request.user
    user_object = request.user
    current_user = Profile.objects.get(user__id=request.user.id)
    user = Profile.objects.get(user__id=id)
    posts = Post.objects.filter(user = user.user)
    return render(request, "profile.html", locals())


# @login_required(login_url='/accounts/login')
def edit_profile(request):
    disp_user = request.user
    current_user=request.user
    user_edit = Profile.objects.get(user__id=current_user.id)
    title = "Edit Profile"
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
            return redirect('profile', user_edit.id)
    else:
        form=ProfileForm(instance=request.user.profile)
        print('error')
    return render(request,'edit_profile.html',locals())

# @login_required(login_url='/accounts/login')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.neighborhood = request.user.profile.neighborhood
            post.save()
        return redirect('post', id)
    else:
        form = PostForm()
    return render(request,'new_post.html', locals())

# @login_required(login_url='/accounts/login')
def new_business(request):
    
    return render(request, 'new_business.html', locals())
