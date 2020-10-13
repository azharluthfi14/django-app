from django.shortcuts import render, redirect
from django.http import JsonResponse
import pandas as pd
from .models import *
import joblib
from .forms import form_user_create, form_user_update,user_update_profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import json
# from .serializers import user_serializer


def index(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('app:dashboard')
    return render(request, 'index.html')


def sign_up_user(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('app:dashboard')
    form = form_user_create()
    if request.method == 'POST':
        form = form_user_create(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('app:signin')
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)


def sign_in_user(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('app:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=username).username
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:dashboard')
        else:
            messages.error(request, "Username or password is invalid ")
    context = {}
    return render(request, 'account/signin.html')

@login_required(login_url='app:signin')
def profile(request):
    if request.method == 'POST':
        user_form = form_user_update(request.POST, instance=request.user)
        image_form = user_update_profile(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and image_form.is_valid():
            user_form.save()
            image_form.save()
            messages.success(request, f'Your profile was updated successfully')
            return redirect('app:profile')
    else:
        user_form = form_user_update(instance=request.user)
        image_form = user_update_profile(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'image_form': image_form
    }

    return render(request, 'account/profile.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('app:signin')

@login_required(login_url='app:signin')
def dashboard(request):
    return render(request, "dashboard.html")


@login_required(login_url='app:signin')
def predict(request):
    return render(request, 'forms.html')

def predict_chances(request):

    if request.POST.get('action') == 'POST':

        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))

        model = pd.read_pickle(
            r"F:\Django_Project\Python3.8\app\model\wine.pickle")

        result = model.predict(
            [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])

        classification = result[0]

        PredResults.objects.create(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid,
                                   residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol, classification=classification)

        return JsonResponse({'result': classification, 'fixed_acidity': fixed_acidity, 'volatile_acidity': volatile_acidity, 'citric_acid': citric_acid, 'residual_sugar': residual_sugar, 'chlorides': chlorides, 'free_sulfur_dioxide': free_sulfur_dioxide, 'total_sulfur_dioxide': total_sulfur_dioxide, 'density': density, 'pH': pH, 'sulphates': sulphates, 'alcohol': alcohol}, safe=False)