import requests,json
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

def movie_list(request):
	try:
		ctx = {}
		ctx['title'] = 'Movie List Page'
		response = requests.get(settings.API_URL)
		if response.status_code == 200:
			ctx['data'] = response.json() 
		return render(request,'movie_list.html',ctx)
	except Exception as e:
		print("Something Went wrong")

def add_movie(request):
	try:
		ctx = {}
		ctx['title'] = 'Add Page'
		ctx['action'] = 'Add'
		if request.method == "POST":
			data = dict(request.POST)
			del data['csrfmiddlewaretoken']
			response = requests.post(url=settings.API_URL,data=data)
			if response.status_code == 201:
				messages.success(request, 'Movie added successfully')
				return redirect('movie_list')
			messages.error(request, 'Please provide valid data')
		return render(request,'add_edit_movie.html',ctx)
	except Exception as e:
		print("Something Went wrong")

def edit_movie(request,pk=None):
	try:
		ctx = {}
		ctx['title'] = 'Edit Page'
		ctx['action'] = 'Edit'
		if pk:
			if request.method == "POST":
				data = dict(request.POST)
				del data['csrfmiddlewaretoken']
				response = requests.put(settings.API_URL+str(pk)+"/",data=data)
				if response.status_code == 200:
					messages.success(request, 'Movie updated successfully')
				else:
					messages.error(request, 'Something went wrong')
				return redirect('movie_list')
			response = requests.get(settings.API_URL+str(pk)+"/")
			if response.status_code == 200:
				ctx['data'] = response.json()
				return render(request,'add_edit_movie.html',ctx)
		return redirect('movie_list')
	except Exception as e:
		print("Something Went wrong")

def delete_movie(request,pk=None):
	try:
		if pk:
			response = requests.delete(settings.API_URL+str(pk)+"/")
			if response.status_code == 204:
				messages.success(request, 'Movie data deleted successfully')
			else:
				messages.error(request, 'Something went wrong')
		return redirect('movie_list')
	except Exception as e:
		print("Something Went wrong")
