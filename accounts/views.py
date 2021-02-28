from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, teacher_only
from .models import *
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')
@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('teacher_panel')
        else:
            messages.info(request, 'Username Or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@teacher_only
def teacherPanel(request):
    exercises = Exercise.objects.all()
    total_exercises = exercises.count()
    context = {'exercises': exercises, 'total_exercises': total_exercises}
    return render(request, 'accounts/teacherpanel.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentPanel(request):
    exercises = request.user.student.exercises.all()
    context = {'exercises': exercises}
    return render(request, 'accounts/studentpanel.html', context)
def exercise(request, pk):
    exercise = Exercise.objects.get(id=pk)
    students = exercise.student_set.all()
    context = {'students': students}
    return render(request, 'accounts/exercises.html', context)