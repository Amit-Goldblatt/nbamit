from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from nbamit import schedule_scraper
from nbamit.forms import NewUserForm
from .models import Team, Game, Rtg_history
from datetime import date, timedelta
from django.contrib.auth.forms import AuthenticationForm


startdate = date.today()
enddate = startdate + timedelta(days=6)
# Create your views here.
def index(request):
    
    teams = Team.objects.all().order_by('-rating')
    games = Game.objects.all().order_by('date').filter(date__range=[startdate, enddate])
    return render(request, 'index.html', {'teams': teams, 'games': games, 'username': request.user.username})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             redirect('index', username)
#         else:
#             # Return an 'invalid login' error message. 
#             return render(request, 'login.html', {'error': 'Invalid username or password'}) 
#     else:
#         return render(request, 'registration\login.html')
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

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
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})