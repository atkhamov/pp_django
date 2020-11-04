from django.shortcuts import render

def index(request):
    return render(request, 'newsreports/newsreports.html')

def newsreport(request):
    return render(request, 'newsreports/newsreport.html')