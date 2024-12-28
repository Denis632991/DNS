from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Product
from .forms import SearchForm

def search(request):
    form = SearchForm()
    results = []

    if 'name' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            results = Product.objects.filter(name= name)

    return render(request, 'main.html', {'form': form, 'results': results})