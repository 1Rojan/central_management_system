from http import server
from django.shortcuts import render
from .models import *

def list_server(request):
  servers = Server.objects.all()
  context = {
    'servers': servers
  }
  return render(request, 'server/server_list.html', context)