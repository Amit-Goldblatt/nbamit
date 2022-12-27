from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from nbamit import schedule_scraper
from nbamit.forms import NewUserForm
from .models import Team, Game, Rtg_history
from datetime import date, timedelta
from django.contrib.auth.forms import AuthenticationForm
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

startdate = date.today()
enddate = startdate + timedelta(days=6)
# Create your views here.
def index(request):
	history = Rtg_history.objects.all().order_by('date')
	teams = Team.objects.all().order_by('-rating')
	games = Game.objects.all().order_by('date').filter(
	date__range=[startdate, enddate])
	# covert to dataframe
	# df = pd.DataFrame.from_records(history.values())
	# print(df)
	# create figure
	fig = make_subplots()
	for team in teams:
		team_history = history.filter(team=team, date__range=['2022-10-18', date.today()])
		df = pd.DataFrame.from_records(team_history.values())
		fig.add_trace(go.Scatter(x=df['date'], y=df['rtg'], name=team.name, visible='legendonly' ))
		fig.update_layout(xaxis_title='Date', yaxis_title='Rating')
	
	
	return render(request, 'index.html', {'teams': teams, 'games': games, 'username': request.user.username, 'fig': fig.to_html(full_html=False, default_height=1000, default_width="100%", include_plotlyjs='cdn')})

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

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")