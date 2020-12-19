from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import Group
from .models.product import Product, Contact
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category',]

class AdminCategory(admin.ModelAdmin):
    list_display = ['name',]

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email',]

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','status',]
    search_fields = ['product', 'customer',]
    actions = ['completed','pending']

    def completed(self, request,queryset):
        queryset.update(status = True)
    def pending(self, request,queryset):
        queryset.update(status = False)

class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )
    

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Contact)
admin.site.register(Order, AdminOrder)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.unregister(Group)
