from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product, Contact
from store.models.orders import Order

class Contactview(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post (self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if request.method=="POST":
            contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, desc=desc)
            contact.save()
        return render(request, 'contact.html')
    # return redirect('/contact')
    # def post(self, request):
        
