from django.shortcuts import render
from .models import ItemRank
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("HIHIHI")

def crawl_main(request):
    rk = ItemRank.objects.all()
    return render(request, 'main_app/tables.html', {'rk':rk})

def crawl_main_c(request):
    rk = ItemRank.objects.all()
    return render(request, 'main_app/charts.html', {'rk':rk})

def crawl_main_d(request):
    rk = ItemRank.objects.all()
    return render(request, 'main_app/index.html', {'rk':rk})

