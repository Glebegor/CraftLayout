from django.shortcuts import render, redirect
from .forms import ProfileImage, FormRegister, ProfileBanner, FirstProfileform, SecondProfileform
from exchange.models import Exchange

def RegisterPage(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormRegister()
    return render(request, 'users/reg.html', {'form':form})




def profile(request):
    ExchangeOrd = Exchange.objects.filter(user=request.user)
    data = {'ExchangeOrd': ExchangeOrd,}
    return render(request, 'users/profile.html', data)

def AvatarPage(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        if img_profile.is_valid():
            img_profile.save()
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
    return render(request, 'users/Avatar.html', {'img_profile': img_profile})

def BannerPage(request):
    if request.method == "POST":
        banner_profile = ProfileBanner(request.POST, request.FILES, instance=request.user.profile)
        if banner_profile.is_valid():
            banner_profile.save()
            return redirect('profile')
    else:
        banner_profile = ProfileBanner(instance=request.user.profile)
    return render(request, 'users/Banner.html', {'banner_profile': banner_profile})

def ChangeProfPage(request):
    if request.method == "POST":
        First_form = FirstProfileform(request.POST, instance=request.user.profile)
        if First_form.is_valid():
            First_form.save()
            return redirect('profile')
    else:
        First_form = FirstProfileform()

    if request.method == "POST":
        Second_form = SecondProfileform(request.POST, instance=request.user)
        if Second_form.is_valid():
            Second_form.save()
            return redirect('profile')
    else:
        Second_form = SecondProfileform()

    data = {
        "First_form": First_form,
        "Second_form": Second_form
    } 
    return render(request, 'users/updateProfile.html', data)