from django.shortcuts import render
from django.http import HttpResponse
from .models import DoubanShort

# Create your views here.
def movies(request):
    queryset = DoubanShort.objects.all()
    # queryset = T1.objects.values('sentiment')
    condtions = {'stars__gte': 4}
    res = queryset.filter(**condtions)
    print (res)
    return render(request, 'index.html', locals())

def test_save_data(request):
    DoubanShort.objects.create(short="", stars=1)
    return HttpResponse("save data")