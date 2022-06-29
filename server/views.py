from http import server
import imp
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Q
from .forms import ServerForm
from django.views.generic.edit import UpdateView
from django.core.exceptions import PermissionDenied

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

# form = UserCreationForm(request.POST or None)
#   if request.method == 'POST':
#     if form.is_valid():
#       form.save()
#       return redirect('blog:home')
#     else:
#       return render(request, 'blog/signup.html', {'user_form':form, 'errors':form.errors})
#   return render(request, 'blog/signup.html', {'user_form':form})
    





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





  # server = get_object_or_404(Server, pk=server_id)
  # form = ServerForm(instance=server)
  # if request.method == 'POST':
  #   if form.is_valid():
  #     form.save()
  #     return HttpResponseRedirect('server_list')
  #   else:
  #     print('-=-=-=-=-=-=-=-=-=-')
  #     print(form.errors)
  # else:
  #   context = {
  #     'form':form
  #   }
  #   return render(request, 'server/server_edit.html', context)

def delete_server(request, server_id):
  pass
