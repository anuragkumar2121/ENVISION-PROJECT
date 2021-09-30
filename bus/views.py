from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NameForms
from .models import NameForm, Passenger, BusStop, Ticket
from django.contrib.auth.models import User
from .models import *

#This is view for homepage and the POST method is for query form on home page.
def index(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "buses/index.html", {
        "schedul": Schedule.objects.all(),
        "busStops": BusStop.objects.all()
    })

# profile view, sending all booked bus schedules and personal info to template user.html
def profile(request):
    Username = request.user.username
    passengerUser=Passenger.objects.filter(username=Username)[0]
    myBuses = passengerUser.buses.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "buses/user.html",{
        "passengerUser": passengerUser,
        "myBuses": myBuses
    })

# View for login, username and password verified
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request,"buses/index.html",{
                "message": "Invalid credentials."
            })
    return render(request, "registration/login.html")

# logout using default django function
def logout_view(request):
    logout(request)
    return render(request,"registartion/login.html",{
        "message": "Logged out."
    })

# Using POST for taking data and forming Passenger Object and login credentials
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data["first_name"]
            u = form.cleaned_data["username"]
            l = form.cleaned_data["last_name"]
            e = form.cleaned_data["email"]
            passen = Passenger(custfName=f, custlName=l, custEmail=e, username=u)
            passen.save()
            form.save()     
    else:
        form = RegisterForm()
    return render(request, "register/register.html",{"form":form})

# Subtracting booked seats from total seats to get available seats
def bus(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    Username = request.user.username
    non_passenger=Passenger.objects.filter(username=Username)
    tickets = Ticket.objects.filter(schedule=schedule)
    totalSeats = schedule.busInfo.seats
    for ticket in tickets:
        totalSeats -= ticket.number
    schedule.seatsEmpty = totalSeats
    return render(request, "buses/bus.html", {
        "schedule": schedule,
        "non_passengers": non_passenger,
        "busStops": BusStop.objects.all(),
    })

# make ticket object based on POST request from bus detail webpage
def book(request, schedule_id):
    if request.method == "POST":
        schedule = Schedule.objects.get(pk=schedule_id)
        passenger = Passenger.objects.get(pk=(int)(request.POST["passenger"]))
        seatNum = (int)(request.POST["ticketNum"])
        ticket = Ticket(schedule=schedule,passenger=passenger,number=seatNum)
        ticket.save()
        passenger.buses.add(schedule)
        return HttpResponseRedirect(reverse("bus", args=(schedule.id,)))

# Getting origin destination and date from POST and giving buses on that time
def search(request):
    if request.method == "POST":
        Origin = request.POST["origin"]
        Destiantion = request.POST["destination"]
        Date = request.POST["date"]
        return render(request, "buses/searchResult.html", {
            "schedule": Schedule.objects.filter(destination=Destiantion, origin=Origin, date=Date).all()
        })
    return render(request, "buses/search.html", {
        "busStops": BusStop.objects.all(),
        "busStops": BusStop.objects.all()
    })

# Gettinf POST request with data of query form and making NameForm object of the same
def form(request):
    if request.method == "POST":
        n = request.POST["name"]
        e = request.POST["email"]
        s = request.POST["subject"]
        m = request.POST["message"]
        t = NameForm(name=n, email=e, subject=s, message=m)
        t.save()
        return render(request, "buses/index.html", {
            "message": "Query Sent."
        })

    else:
        return render(request, "buses/index.html")
