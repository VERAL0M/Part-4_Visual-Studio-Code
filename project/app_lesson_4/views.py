from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')





















# from django.shortcuts import render
# from django.http import HttpResponse


# def func(request):
#     return HttpResponse('Домашка по 4 занятию')
