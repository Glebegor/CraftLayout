from .models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileImage, FormRegister, ProfileBanner, FirstProfileform, SecondProfileform
from exchange.models import Exchange
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def RegisterPage(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            username  = form.cleaned_data.get("username")
            password  = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = FormRegister()
    return render(request, 'users/reg.html', {'form':form})

def profile(request, slugFil):
    UserOrd = User.objects.filter(username=slugFil)
    NameProf = UserOrd[0]
    EmailProf = UserOrd[0].email
    ExchangeOrd = Exchange.objects.filter(user=NameProf)
    ProfileOrd = Profile.objects.filter(user=NameProf)
    ProfileOrd = ProfileOrd[0]
    data = {
        'EmailProf': EmailProf,
        'ExchangeOrd': ExchangeOrd,
        'UserOrd': UserOrd,
        'NameProf': NameProf,
        'ProfileOrd': ProfileOrd
    }
    return render(request, 'users/profile.html', data)

def AvatarPage(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        if img_profile.is_valid():
            img_profile.save()
            return redirect('home')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
    return render(request, 'users/Avatar.html', {'img_profile': img_profile})

def BannerPage(request):
    if request.method == "POST":
        banner_profile = ProfileBanner(request.POST, request.FILES, instance=request.user.profile)
        if banner_profile.is_valid():
            banner_profile.save()
            return redirect('home')
    else:
        banner_profile = ProfileBanner(instance=request.user.profile)
    return render(request, 'users/Banner.html', {'banner_profile': banner_profile})

def ChangeProfPage(request):
    if request.method == "POST":
        First_form = FirstProfileform(request.POST, instance=request.user.profile)
        if First_form.is_valid():
            First_form.save()
            return redirect('home')
    else:
        First_form = FirstProfileform()

    if request.method == "POST":
        Second_form = SecondProfileform(request.POST, instance=request.user)
        if Second_form.is_valid():
            Second_form.save()
            return redirect('home')
    else:
        Second_form = SecondProfileform()

    data = {
        "First_form": First_form,
        "Second_form": Second_form
    } 
    return render(request, 'users/updateProfile.html', data)