from statistics import mode
from django.db import models


class CommonInfo(models.Model):
  name = models.CharField(max_length=63)

class ServerType(CommonInfo):
  pass

class Diskype(CommonInfo):
  pass

class Owner(CommonInfo):
  pass

class Location(CommonInfo):
  pass

