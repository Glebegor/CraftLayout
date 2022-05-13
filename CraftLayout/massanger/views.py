from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import Profile
from .forms import massangerForm
from .models import MassangerModel

def MassangPage(request, ToUser_name):
    allUsers = User.objects.all()
    UserOrd = User.objects.filter(username=ToUser_name)
    NameProf = UserOrd[0]
    Name2 = ToUser_name
    sendTo = MassangerModel.objects.filter(username=request.user)
    sendToSend = []
    for i in sendTo:
        sendToSend.append(i.SendTo)

    sendToSendClear = [] 
    for item in sendToSend: 
        if item not in sendToSendClear: 
            sendToSendClear.append(item) 
    print(sendToSendClear)
    MassangerOrd = MassangerModel.objects.all()
    ProfileOrd = Profile.objects.filter(user=NameProf)
    YourName = request.user
    if request.method == "POST":
        form = massangerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = massangerForm()
    data = {
        'sendToSendClear': sendToSendClear,
        'sendTo': sendTo,
        'allUsers': allUsers,
        'Name2': Name2,
        'YourName': YourName,
        'form_mass': form,
        'UserOrd': UserOrd,
        'NameProf': NameProf,
        'ProfileOrd': ProfileOrd[0],
        'MassangerOrd': MassangerOrd
    }
    return render(request, 'massanger/massang.html', data)