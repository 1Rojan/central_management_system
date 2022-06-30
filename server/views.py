from http import server
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Q
from .forms import ServerForm
from django.views.generic.edit import UpdateView
from django.core.exceptions import PermissionDenied
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def list_server(request):
  server_form = ServerForm()
  servers = Server.objects.all()
  context = {
    'servers': servers,
    'server_form': server_form
  }
  return render(request, 'server/server_list.html', context)


def search_server(request):
  if request.method == 'POST':
    search_key = request.POST['search_key']
    servers = Server.objects.filter(Q(name__icontains=search_key)|Q(username__icontains=search_key)|Q(server_type__name__icontains=search_key)|Q(public_ip__icontains=search_key))
    context = {
      'search_key': search_key,
      'servers':servers
    }
    return render(request, 'server/server_list.html', context)

@login_required
def add_server(request):
  form = ServerForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('server_list')
  else:
    return render(request, 'server/add_server.html', {'server_form':form, 'errors':form.errors})
  server_form = ServerForm()
  context = {
    'server_form': server_form
  }
  return render(request, 'server/add_server.html', context)


def server_detail_view(request, server_id):
  server = get_object_or_404(Server, pk=server_id)
  context = {
    'server':server
  }
  return render(request, 'server/server_detail.html', context)


@login_required
def update_server(request, server_id):
  server = Server.objects.get(pk=server_id)
  if request.method == 'POST': 
    form = ServerForm(request.POST, request.FILES, instance=server) 
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = ServerForm(instance=server) 
    context = {
      'form':form
    }
    return render(request, 'server/server_edit.html', context)


def delete_server(request, server_id):
  pass


def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("server_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="server/signup.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("server_list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "server/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("server_list")