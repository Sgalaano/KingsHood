from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

# Create your views here.

def index(request):
    # current_user = request.user
    # profile = Profile.objects.get(user = current_user)
    #
    # posts = Post.objects.filter(neighborhood = profile.neighborhood)
    # businesses = Business.objects.filter(neighborhood = profile.neighborhood)
    # hood = profile.neighborhood

    return render(request,'index.html', locals())


# @login_required(login_url='/accounts/login')
def search(request):

    return render(request, 'search.html', locals())

# @login_required(login_url='/accounts/login')
def business(request):

    return render(request, 'business.html', locals())

# @login_required(login_url='/accounts/login')
def post(request, id):

    return render(request, 'post.html', locals())

# @login_required(login_url='/accounts/login')
def profile(request, id):

    return render(request, 'profile.html', locals())

# @login_required(login_url='/accounts/login')
def edit_profile(request):

    return render(request,'edit_profile.html',locals())

# @login_required(login_url='/accounts/login')
def new_post(request):

    return render(request,'new_post.html', locals())

# @login_required(login_url='/accounts/login')
def new_business(request):

    return render(request, 'new_business.html', locals())
