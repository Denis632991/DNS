from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Product
from django.shortcuts import render
from django.db.models import Q
from .models import Product
from .forms import SearchForm


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'describe', 'price', 'number']
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'describe', 'price', 'number']
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm.html'
    success_url = reverse_lazy('product-list')
    context_object_name = 'products'

def search(request):
    form = SearchForm()
    results = []

    if 'name' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            results = Product.objects.filter(name= name)

    return render(request, 'product_list.html', {'form': form, 'results': results})

