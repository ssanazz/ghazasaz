from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import *

def signup(request):
    return render(request, 'signup.html')

def signup_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            # auth_login(request, user)
            return redirect('HomePage')
    else:
        form = RestaurantForm()
    return render(request, 'signup_form.html', {'form': form, 'type': 'رستوران'})

def signup_user(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.address = form.cleaned_data.get('address')
            user.customer.city = form.cleaned_data.get('city')
            user.customer.image=form.cleaned_data.get('image')
            user.save()
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('HomePage')
    else:
        form = CustomerForm()
    return render(request, 'signup_form.html', {'form': form, 'type': 'کاربر'})