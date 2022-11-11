
from datetime import datetime, timedelta
from venv import create
from django.shortcuts import render, redirect
from .templatetags.tags import to_str
from summaryapp.models import assignment, service
from .forms import RegisterForm, AssignmentForm, ServiceFrom
from summaryapp.models import AssingmentModel, ServiceModel
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def home(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
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

    Sum = []
    sum_month = []
    now = datetime.now()
    month = now.month
    
    if request.user.is_superuser:
        assignments_month = AssingmentModel.objects.filter(created_at__month = month).order_by('employee')   
    else:
        assignments_month = AssingmentModel.objects.filter(employee = request.user).filter(created_at__month = month)

    for assignment in assignments:
        prize = 0
        # for service in assignment.service.all():
        prize = assignment.service.prize
        prize += assignment.tip
        Sum.append(prize)

    for assignment in assignments_month:
        prize_month = 0
        # for service in assignment.service.all():
        prize_month += assignment.service.prize
        prize_month += assignment.tip
        sum_month.append(prize_month)

    if request.user.is_staff and not request.user.is_superuser:
        Sum.clear()
    return render(request, 'summaryapp/home.html', {"assignments": assignments, "sum": Sum, "sum_month": sum_month, "form": form})


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


@login_required(login_url="/login")
def dashboard(request):
    assignments = AssingmentModel.objects.all().order_by('-created_at')[:5]
    Sum = [23, 13, 45, 13, 76, 8, 30]

    now = datetime.now()
    today = now.day
   
    assignments_day = AssingmentModel.objects.filter(created_at__day = today)

    month = now.month
    assignments_month = AssingmentModel.objects.filter(created_at__month = month)
   
    sum_month = []
    sum_day = []
    prize_day = 0
    prize_month = 0

    for assignment in assignments_day:
        prize_day += assignment.service.prize
        prize_day += assignment.tip
        sum_day.append(prize_day)

    for assignment in assignments_month:
        prize_month += assignment.service.prize
        prize_month += assignment.tip
        sum_month.append(prize_month)

# ---------------------------------------------------------------
    assignments_day_before = AssingmentModel.objects.filter(created_at__day = (int(today)-1))
    assignments_month_before = AssingmentModel.objects.filter(created_at__month = (int(month)-1))

    sum_month_before = []
    sum_day_before = []
    
    prize_day_before = 0
    prize_month_before = 0

    for assignment in assignments_day_before:
        # for service in assignment.service.all():
        prize_day_before += assignment.service.prize
        prize_day_before += assignment.tip
        sum_day_before.append(prize_day_before)

    for assignment in assignments_month_before:
        # for service in assignment.service.all():
        prize_month_before += assignment.service.prize
        prize_month_before += assignment.tip
        sum_month_before.append(prize_month_before)

    return render(request, 'dashboard/home.html', {"assignments": assignments, "sum_day": sum(sum_day), "sum_month": sum(sum_month), 'month_sum_before':sum(sum_month_before), 'day_sum_before':sum(sum_day_before), "sum": Sum})

@login_required(login_url="/login")
def services(request):
    if request.method == "POST":
        form = ServiceFrom(request.POST)
        form.save()
        return redirect("/services")
    else:
        form = ServiceFrom()
    
    
    services = ServiceModel.objects.all()
    return render(request, 'dashboard/services.html', {"services": services, "form": form})

@login_required(login_url="/login")
def edit_service(request, pk):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            obj = ServiceModel.objects.get(id=pk)
            obj.name = request.POST['Name']
            Hour = request.POST['Hour']
            Minute = request.POST['Minute']
            obj.time = timedelta(hours=int(Hour), minutes=int(Minute))
            obj.prize = request.POST['Prize']
            obj.save()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

@login_required(login_url="/login")
def delete_service(request, pk):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            obj = ServiceModel.objects.get(id=pk)
            obj.delete()
            return JsonResponse({'status':'Success', 'msg': 'save successfully'})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

@login_required(login_url="/login")
def summary(request):
    from django.http import JsonResponse
    if request.method=='POST':
        try:
            month = request.POST['Month']
            day= request.POST['Day']

            assignments_day = AssingmentModel.objects.filter(created_at__day = day)
            assignments_month = AssingmentModel.objects.filter(created_at__month = month)

            sum_month = []
            sum_day = []
            prize_day = 0
            prize_month = 0

            for assignment in assignments_day:
                
                # for service in assignment.service.all():
                prize_day += assignment.service.prize
                prize_day += assignment.tip
                sum_day.append(prize_day)

            for assignment in assignments_month:
                
                # for service in assignment.service.all():
                prize_month += assignment.service.prize
                prize_month += assignment.tip
                sum_month.append(prize_month)
# --------------------------------------------------------------------------------------------------
            # assignments_day_before = AssingmentModel.objects.filter(created_at__day = (int(day)-1))
            # assignments_month_before = AssingmentModel.objects.filter(created_at__month = (int(month)-1))

            # sum_month_before = []
            # sum_day_before = []
            # prize_day_before = 0
            # prize_month_before = 0

            # for assignment in assignments_day_before:
                
            #     # for service in assignment.service.all():
            #     prize_day_before += assignment.service.prize
            #     prize_day_before += assignment.tip
            #     sum_day_before.append(prize_day_before)

            # for assignment in assignments_month_before:
                
            #     # for service in assignment.service.all():
            #     prize_month_before += assignment.service.prize
            #     prize_month_before += assignment.tip
            #     sum_month_before.append(prize_month_before)

            return JsonResponse({'month_sum':sum(sum_month), 'day_sum':sum(sum_day)})
        except ServiceModel.DoesNotExist:
            return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})
    else:
         return JsonResponse({'status':'Fail', 'msg':'Not a valid request'})

@login_required(login_url="/login")
def transactions(request):
    assignments = AssingmentModel.objects.all()
    return render(request, 'dashboard/transactions.html', {"assignments": assignments})

