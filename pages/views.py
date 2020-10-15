from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def newsreport(request):
    return render(request, 'pages/newsreport.html')

