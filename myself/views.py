# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from myself.models import Post
from myself.forms import PostForm
import datetime

from django.http import HttpResponse
# Create your views here.

def index(request) :
    my_dict = dict()
    my_dict["name"] = "AlvaroC"
    my_dict["fruits"] = ["apple", "ice cream"]
    my_dict["all_posts"] = Post.objects.all()


    return render(request, 'index.html', my_dict)

def new_post(request):
    if request.method == 'POST':
        filled_form = PostForm(request.POST)
        post = filled_form.save(commit=False)
        post.date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect('/myself')
    data = dict()
    new_post= PostForm()
    data["post_form"] = new_post
    return render(request, 'new_post.html', data)

