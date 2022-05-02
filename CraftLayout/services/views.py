from django.shortcuts import render
def HomePage(request):
    Title = 'Home Page'
    return render(request, 'services/home.html', {'Title':Title})
