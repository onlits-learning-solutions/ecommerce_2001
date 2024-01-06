from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from products.models import Product

# Create your views here.


def index(request):
    products = Product.objects.all().values()
    template = loader.get_template("products_index.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))


def create(request):
    return render(request, "products_create.html")


def save(request):
    product = Product(name=request.POST["name"], brand=request.POST["brand"])
    product.save()

    products = Product.objects.all()
    template = loader.get_template("products_index.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))


def edit(request, id):
    product = Product.objects.get(id=id)
    template = loader.get_template("products_edit.html")
    context = {
        "product": product,
    }
    return HttpResponse(template.render(context, request))


def update(request, id):
    product = Product.objects.get(id=id)
    product.name = request.POST["name"]
    product.brand = request.POST["brand"]
    product.save()

    products = Product.objects.all()
    template = loader.get_template("products_index.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))
