from statistics import mode
from django.db import models


class CommonInfo(models.Model):
  name = models.CharField(max_length=63)

  def __str__(self):
    return self.name

class ServerType(CommonInfo):
  pass

class DiskType(CommonInfo):
  pass

class Owner(CommonInfo):
  pass

class Location(CommonInfo):
  pass

class Server(models.Model):

  options = (
    ('gb', 'GB'),
    ('tb', 'TB'),
  )

  status = (
    (0, 'Inactive'),
    (1, 'Active'),
  )

  name = models.CharField(max_length=63)
  
  cpu = models.CharField(max_length=63)
  ram = models.CharField(max_length=3, choices=options, default='gb')
  ip_address = models.CharField(max_length=63)
  username = models.CharField(max_length=63)
  password = models.CharField(max_length=63)
  public_ip = models.CharField(max_length=63)
  private_ip = models.CharField(max_length=63)
  status = models.BooleanField(default=0, choices=status)
  server_location = models.ForeignKey(Location, on_delete=models.CASCADE)
  server_type = models.ForeignKey(ServerType, on_delete=models.CASCADE)
  disk_type = models.ForeignKey(DiskType, on_delete=models.CASCADE)
  Owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
  remarks = models.TextField(blank=True, null=True)


  def __str__(self):
    return self.name

