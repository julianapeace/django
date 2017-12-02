from django.shortcuts import render
from temple.models import Class
from django.views import generic
import requests

# Create your views here.

#the / url leads here
def index(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'index.html', context={'num_visits': num_visits})
#the url /classes leads here
def classes (request):
    print('hello')
    r = Class.objects.all().count()
    narf = r
    return render(request,'classes.html', context={'narf':narf,})

class ClassListView(generic.ListView):
    model = Class

#This class didn't work bc djzen doesn't support <pk>. must be <int>
# class ClassDetailView(generic.DetailView):
#     model = Class

def book_detail_view(request,int):
    try:
        class_id=Class.objects.get(pk=int)
    except Class.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'temple/class_detail.html',
        context={'class':class_id,}
    )
