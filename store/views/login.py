from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

class login(View):
    # return_url = None

    def get(self, request):
        # login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('/')


                # if login.return_url:
                #     return HttpResponseRedirect(login.return_url)
                # else:
                #     login.return_url = None
                    
            else:
                error_message = 'Email or Password is invalid !!'
        else:
            error_message = 'Email or Password is invalid !!'
        print(email, password)
        return render (request, 'login.html', {'error' : error_message})


def logout(request):
    request.session.clear()
    return redirect('/login')