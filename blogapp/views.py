from django.contrib import messages
from django.utils.html import json_script
from django.views import generic
from scipy.constants import slug
import json
from blogapp.models import User, comment,Entry
from . import models
from django.shortcuts import render, redirect, get_object_or_404
from .forms import postform, commentform
from django.contrib.auth import authenticate, login
from .forms import UserForm
import logging
logger=logging.getLogger(__name__)




class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 12


class BlogUser(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "user.html"
    paginate_by = 12


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/user')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)



def swallow(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html')
            else:
                return render(request, 'login1.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login1.html', {'error_message': 'Invalid login'})
    return render(request, 'login1.html')




def Postsubmit(request):
    if request.method == 'POST':
        form = postform(request.POST or None)
        print(form.data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/')
        context={
            "form": form,
        }
        return redirect('/add')


def AddComment(request,slug):
    
    form = commentform(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/user',{slug:slug})
        else:
            return redirect('/',{slug:slug})
    else:
        form=commentform
        template_name= 'AddComment.html'
        context={
            "form": form
        }
        return render(request,template_name, {'slug':slug, 'comment_form':form})


def postadd(request):
    return render(request, 'post.html')


class detail(generic.ListView):
    queryset = comment.objects.all()
    template_name = "post_detail.html"
    paginate_by = 30


def compo(request, slug):
    return render(request, 'comment.html')

def edit(request, ID):
   if request.method == 'POST':
        form=commentform(instance=get_object_or_404(comment, ID=ID), data=request.POST.dict())
        comment.objects.filter(ID=form.instance.ID).update(comment=form.data['comment'])
        return redirect('/user')
   else:
        return render(request,'comment.html',{'ID':ID, 'form': commentform})
        
def delete(request, ID):  
   
   Comment= get_object_or_404(comment, ID=ID)
   print(Comment)
   Comment.delete()
          
   return redirect('/user')
   