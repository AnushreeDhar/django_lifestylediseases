
from django.shortcuts import render
from django.http import HttpResponse
from .models import CardiovascularD 
def index(request):
    return HttpResponse("<h2>Lifestyle diseases</h2>")
    from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_cd=CardiovascularD.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available=CardiovascularD.objects.filter(status__exact='a').count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'number of cardiovascular diseases':num_cd,'num_instances':num_instances,
        'num_instances_available':num_instances_available},
    )

def index(request):
    ...

    num_authors=CardiovascularD.objects.count()  # The 'all()' is implied by default.
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'number of cardiovascular diseases':num_cd,
        'num_instances_available':num_instances_available,
            'num_visits':num_visits}, # num_visits appended
    )