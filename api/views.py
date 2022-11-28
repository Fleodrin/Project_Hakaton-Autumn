from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from challenge.models import Participant


def getchal(request):
  participant = Participant.objects.all().order_by('balls')
  print(participant)
  participant_json = serializers.serialize('json', participant)
  return HttpResponse(participant_json)
