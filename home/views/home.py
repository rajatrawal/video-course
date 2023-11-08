from django.shortcuts import render,redirect
from home.models import Course
from django.db.models import Q
from django.views.generic import ListView
# Create your views here.



def search(request):
    query = request.GET.get('search')
    if query is None:
        return redirect('home')
    courses = Course.objects.filter(Q(name__contains=query)|Q(description__contains=query))
    params = {'courses':courses,'query':query}
    return render(request,'home/index.html',params)

class HomePageView(ListView):
    template_name = 'home/index.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = "courses"
    