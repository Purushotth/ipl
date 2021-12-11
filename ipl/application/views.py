from django.shortcuts import render

from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *


class DriverView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = DriverForm()
        print(DriverModel.objects.all())
        self.context = {
            'form': form,
            'drivers': DriverModel.objects.all()
        }
        return render(request, "driver.html", self.context)

    def post(self, request, *args, **kwargs):
        self.post_params = request.POST.copy()
        form = DriverForm(self.post_params, request.FILES)
        if form.is_valid():
            form.save()
        self.context = {
            'form': DriverForm(),
            'drivers': DriverModel.objects.all(),
            "upload_status": 1
        }
        return render(request, "driver.html", self.context)


class TruckView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = DriverForm()
        self.context = {
            'form': form,
        }
        return render(request, "driver.html", self.context)

    def post(self, request, *args, **kwargs):
        self.post_params = request.POST.copy()
        form = DriverForm(self.post_params, request.FILES)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data
            return HttpResponse(form_data)


class ConsigneeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ConsigneeForm()
        self.context = {
            'form': form,
        }
        return render(request, "consignee.html", self.context)

    def post(self, request, *args, **kwargs):
        self.post_params = request.POST.copy()
        form = ConsigneeForm(self.post_params, request.FILES)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data
            return HttpResponse(form_data)


class ConsignorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ConsignorForm()
        self.context = {
            'form': form,
        }
        return render(request, "consignor.html", self.context)

    def post(self, request, *args, **kwargs):
        self.post_params = request.POST.copy()
        form = ConsignorForm(self.post_params, request.FILES)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data
            return HttpResponse(form_data)


class LandingPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        print(ShippingOrdersModel.objects.all()[0].payment_status)
        form = ShippingOrdersForm()
        consignee_list = ConsigneeModel.objects.all().values('id', 'name')
        consignor_list = ConsignorModel.objects.all().values('id', 'name')

        self.context = {
            'form': form,
            'consignees': consignee_list,
            'consignors': consignor_list
        }
        return render(request, "landingpage.html", self.context)

    def post(self, request, *args, **kwargs):
        print(ShippingOrdersModel.objects.all())
        self.post_params = request.POST.copy()
        print(22222222)
        print(self.post_params)
        form = ShippingOrdersForm(self.post_params)
        print(form.errors)
        if form.is_valid():
            form.save()
        consignee_list = ConsigneeModel.objects.all().values('id', 'name')
        consignor_list = ConsignorModel.objects.all().values('id', 'name')

        self.context = {
            'form': form,
            'consignees': consignee_list,
            'consignors': consignor_list
        }
        return render(request, "landingpage.html", self.context)