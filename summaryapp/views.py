
from datetime import datetime
from venv import create
from django.shortcuts import render, redirect

from summaryapp.models import assignment, service
from .forms import RegisterForm, AssignmentForm
from summaryapp.models import AssingmentModel, ServiceModel
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def home(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        print(form)
        form.save()
        return redirect("/home")
    else:
        form = AssignmentForm()

    if request.user.is_superuser:
        assignments = AssingmentModel.objects.all().order_by('employee')   
    elif request.user.is_staff:
        now = datetime.now()
        today = now.day
        assignments = AssingmentModel.objects.filter(created_at__day = today)
    else:
        assignments = AssingmentModel.objects.filter(employee = request.user)

    sum = []
    sum_month = []
    now = datetime.now()
    month = now.month
    
    if request.user.is_superuser:
        assignments_month = AssingmentModel.objects.filter(created_at__month = month).order_by('employee')   
    else:
        assignments_month = AssingmentModel.objects.filter(employee = request.user).filter(created_at__month = month)

    for assignment in assignments:
        prize = 0
        for service in assignment.service.all():
            prize += service.prize
        prize += assignment.tip
        sum.append(prize)

    for assignment in assignments_month:
        prize_month = 0
        for service in assignment.service.all():
            prize_month += service.prize
        prize_month += assignment.tip

        sum_month.append(prize_month)
    if request.user.is_staff and not request.user.is_superuser:
        sum.clear()
    return render(request, 'summaryapp/home.html', {"assignments": assignments, "sum": sum, "sum_month": sum_month, "form": form})


def sign_up(request):                                           #///////  53:48   /////// 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form": form})


# @login_required(login_url="/login")
# def add_assignment(request):
#     if request.method == "POST":
#         form = AssignmentForm(request.POST)
#         form.save()
#         return redirect("/home")
#     else:
#         form = AssignmentForm()

#     return render(request, 'summaryapp/add_assignment.html', {"form": form})
