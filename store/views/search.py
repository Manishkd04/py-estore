from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.views.generic import TemplateView
from store.models.product import Product
from django.db.models import Q
from django.http import JsonResponse

class Search(TemplateView):
    template_name = "search.html"

    def get_context_data(self,**kwargs):
        # template_name = request.GET.get("template_name")
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Product.objects.filter(Q(name__icontains=kw) | Q(description__icontains=kw))
        context["results"] = results
        print(kw, "...............")
        return context

def autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(name__istartswith=request.GET.get('term'))
        names = list()
        for product in qs:
            names.append(product.name)
        return JsonResponse(names, safe=False)
    return render(request, 'templates/base.html')