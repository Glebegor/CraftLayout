from django.shortcuts import render

def MassangerPage(request):
    return render(request, 'massanger/main-massanger.html')