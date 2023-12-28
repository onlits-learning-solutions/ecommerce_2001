from django.shortcuts import render
from django.http import HttpResponse
from sellers.models import Seller
from django.template import loader


def index(request):
    sellers = Seller.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "sellers": sellers,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(sellers)


def create(request):
    return render(request, "create.html")


def save(request):
    seller = Seller(
        name=request.POST["name"],
        contact_person=request.POST["contact_person"],
        contact_number=request.POST["contact_number"],
        emailid=request.POST["email"],
        gstin=request.POST["gst"],
        pan=request.POST["pan"],
    )
    seller.save()
    sellers = Seller.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "sellers": sellers,
    }
    return HttpResponse(template.render(context, request))
