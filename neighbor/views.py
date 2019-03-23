from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

# Create your views here.

def index(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    posts = Post.objects.filter(neighborhood = profile.neighborhood)
    businesses = Business.objects.filter(neighborhood = profile.neighborhood)
    hood = profile.neighborhood

    return render(request,'index.html', locals())
