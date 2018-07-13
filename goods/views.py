from django.shortcuts import render, get_object_or_404

from .models import Product


def all_goods(request):
    model = Product.objects.filter(is_published=True)
    return render(request, 'goods/all-goods.html', {'model': model})


def view_prduct(request, pk=None):
    model = get_object_or_404(Product, pk=pk, is_published=True)
    return render(request, 'goods/view.html', {'model': model})
