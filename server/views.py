from http import server
from django.shortcuts import render
from .models import *
from django.db.models import Q

def list_server(request):
  servers = Server.objects.all()
  context = {
    'servers': servers
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