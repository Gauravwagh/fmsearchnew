# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import requests
import urllib, json

from facebook.models import History

def login(request):
	return render(request, 'facebook/login.html')

@login_required
def home(request):
	return render(request, 'facebook/home1.html')

@csrf_exempt
def artist_search(request):
	data_list = []
	artist_name= request.POST['id']
	
	api_url = 'http://ws.audioscrobbler.com/2.0/'
	api_key = 'c712f60d8d4eea6536a59d62a88d4dd7'
	url = api_url+'?method=artist.search&format=json&artist='+artist_name+'&api_key='+api_key
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	
	
	datasave = History(person=request.user, artist_name=artist_name, created_date=timezone.now())
	datasave.save()
	#hist = History(user=request.user, )
	#get_similar = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=cher&api_key=c712f60d8d4eea6536a59d62a88d4dd7&format=json'
	url1 = api_url+'?method=artist.getsimilar&format=json&artist='+artist_name+'&api_key='+api_key
	response = urllib.urlopen(url1)
	data1 = json.loads(response.read())
	#print "artist similar"
	#print data1
	
	url2 = api_url+'?method=artist.gettopalbums&format=json&artist='+artist_name+'&api_key='+api_key
	response = urllib.urlopen(url2)
	data2 = json.loads(response.read())
	#print "artist top album"
	#print data2
	
	url3 = api_url+'?method=artist.getinfo&format=json&artist='+artist_name+'&api_key='+api_key
	response = urllib.urlopen(url3)
	data3 = json.loads(response.read())
	#print "artist info"
	#print data3
	
	
	record1 = {"data3":data3}
	#print record
	#data_name.append(record1)
	
	response = json.dumps(data)
	#print response
	return HttpResponse(response, mimetype="application/json")

@csrf_exempt
def history(request):
	his = History.objects.filter(person=request.user).order_by('-created_date')
	for h in his:
		artist_name = h.artist_name
		api_url = 'http://ws.audioscrobbler.com/2.0/'
		api_key = 'c712f60d8d4eea6536a59d62a88d4dd7'
		url = api_url+'?method=artist.search&format=json&artist='+artist_name+'&api_key='+api_key
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		print data
		response = json.dumps(data)
		return HttpResponse(response, mimetype="application/json")
