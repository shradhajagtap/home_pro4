from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HotelBookingForm
from .models import HotelBooking


@login_required(login_url="user_urls")
def hotel_view(request):
    template_name = "curd_app/hotel_info.html"
    form = HotelBookingForm
    if request.method == "POST":
        form = HotelBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="user_urls")
def show_view(request):
    template_name = "curd_app/show_info.html"
    info = HotelBooking.objects.all()
    context = {"info": info}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = HotelBooking.objects.get(id=pk)
    form = HotelBookingForm(instance=obj)
    if request.method == "POST":
        form = HotelBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    template_name = "curd_app/hotel_info.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request, pk):
    obj = HotelBooking.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_urls")
    return render(request, 'curd_app/cancel.html')
