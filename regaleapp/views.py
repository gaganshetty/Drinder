from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from regaleapp.models import Location, Person, Restaurant, Cusine
from friendship.models import Friend, FriendshipRequest
from django.template import RequestContext



def home(request):
	if request.user.is_authenticated:
		return redirect(f'/dashboard/{request.user.pk}')
	return render(request, 'index.html')

def signup(request):
	location = Location.objects.all()
	if request.method == 'POST':
		fname = request.POST.get('firstname')
		lname = request.POST.get('lastname')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user_exists = User.objects.filter(username=username).exists()
		if not user_exists:
			user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password=password)
			login(request,user)
			return render(request, 'Create_profile.html',{"user":user,"locations":location})
		else:
			return HttpResponse('Username already exists please try some other names')

def signin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		
		if user is not None:
			login(request,user)
			return redirect(f'/dashboard/{user.pk}')
		else:
			message='Enter valid credentials'
			return render(request,'index.html',{"warning":message})
			# return HttpResponse(message)
	else:
		return redirect('/')

def dashboard(request,pk):
	if request.user.is_authenticated:
		user = User.objects.get(pk=pk)
		location_list = Location.objects.all()
		profile = Person.objects.get(user=user)
		if request.method == 'POST':
			location = request.POST.get('location')
			date = request.POST.get('date')
			new_location = Location.objects.get(name=location)
			person = Person.objects.filter(location=new_location, is_available=date)
			print(person)
			if person is None:
				print('2')
				return HttpResponse('Nobody is available')
			# 	message = "No results found"
			# 	return render(request,'dashboard.html',{"message":message})
			else:
				return render(request,'dashboard.html',{"persons":person,"profile":profile,"locations": location_list})
		return	render(request,'dashboard.html',{"locations": location_list,"profile":profile})
	else:
		return redirect('/')

def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/')

def create_profile(request,pk):
	user = User.objects.get(pk=pk)
	if request.method == 'POST':
		bio = request.POST.get('bio')
		location = request.POST.get('location')
		new_location = Location.objects.get(name=location)
		available = request.POST.get('available')
		profile = Person.objects.create(user=user,bio=bio,location=new_location,is_available=available)
		return redirect(f'/dashboard/{pk}')


def profile_edit(request,pk):
	if request.user.is_authenticated:
		profile = Person.objects.get(pk=pk)
		location = Location.objects.all()
		if request.user == profile.user:

			if request.method == 'POST':
				bio = request.POST.get('bio')
				location = request.POST.get('location')
				available = request.POST.get('available')
				profile.bio = bio
				profile.is_available = available
				new_location = Location.objects.get(name=location)
				profile.location = new_location
				profile.save()
				return redirect(f'/profile/{profile.pk}/')
		return render(request,'profile_edit.html',{"profile":profile,"locations":location})
	else:
		return redirect('/')


def profile_view(request,pk):
	if request.user.is_authenticated:
		profile = Person.objects.get(pk=pk)
		if request.method == 'POST':
			other_user = User.objects.get(pk=pk)
			friend_request = Friend.objects.add_friend(request.user,other_user)
			return HttpResponse(f'request has been sent to {profile.user.first_name}')
		return render(request,'profilepage.html',{"profile":profile})
	else:
		return redirect('/') 


def cusines_view(request):
	# if request.user.is_authenticated:
	cusines = Cusine.objects.all()
	return render(request,'cusines.html',{"cusines":cusines})
	# else:
		# return redirect('/')

def profiles_list_view(request):
	# if request.user.is_authenticated:
	profiles = Person.objects.all()
	return render(request,'profile_list.html',{"profiles":profiles})
	# else:
		# return redirect('/')

def error_404(request):
	return  render(request,'404.html')





