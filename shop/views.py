from django.views import View
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

greets = "Welcome to the Bike shop"


class BikesView(View):
    template_name = 'bikes.html'

    def get(self, request, *args, **kwargs):
        context = {'greets': greets, 'bikes': Bike.objects.all}
        return render(request, "shop/bikes.html", context=context)


class BikeView(View):
    template_name = 'bike.html'
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        bike = Bike.objects.filter(id=pk).first()
        return render(request, 'shop/bike.html',
                      context={'bike': bike,
                               'order_form': self.form_class,
                               'is_available': bike.is_available()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pk = self.kwargs['pk']
        bike = Bike.objects.filter(id=pk).first()

        if bike.is_available() and form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            phone_number = form.cleaned_data['phone_number']
            order = Order.objects.create(name=name,
                                         surname=surname,
                                         phone_number=phone_number,
                                         bike=bike)
            order.save()
            bike.bought()
            order_no = order.pk
            return redirect(f'/order/{order_no}/')

        return redirect(f'/bikes/{pk}/')


class OrderView(View):
    template_name = 'order.html'

    def get(self, request, *args, **kwargs):
        order_no = self.kwargs['pk']
        order = Order.objects.filter(pk=order_no).first()
        context = {'order_no': order_no}
        return render(request, 'shop/order.html', context=context)


