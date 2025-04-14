from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import product, Categories
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
import requests
import random
from django.shortcuts import get_object_or_404, redirect


# Create your views here.


def showland(request):
    if 'cart_count' not in request.session:
        request.session['cart_count'] = 0
    template = loader.get_template('landpage.html')
    categories = Categories.objects.all()
    request.session['x'] = 10
    print(request.session['x'])
    data = {
        'categories': categories,
        'cart_count': request.session['cart_count'],
    }
    return HttpResponse(template.render(data, request))

def list_products(request,id):
    if 'cart_count' not in request.session:
        request.session['cart_count'] = 0
    print(request.session['x'])
    template = loader.get_template('list_products.html')
    products= product.objects.filter(categories_id=id)
    data= {
        'product': products,
        'cart_count': request.session['cart_count'],
    }
    return HttpResponse(template.render(data, request))
   
def productdetails(request,id):
    if 'cart_count' not in request.session:
        request.session['cart_count'] = 0
    products= product.objects.select_related('categories').get(id=id)

    data= {
        'cart_count': request.session['cart_count'],
        'product': products,
    }
    template = loader.get_template('productdetails.html')
    return HttpResponse(template.render(data, request))


def add_to_cart(reauest):
    reauest.session['cart_count'] = reauest.session.get('cart_count',0)+ 1
    reauest.session.modified = True
    return JsonResponse({'cart_count': reauest.session['cart_count']})

@login_required
@csrf_exempt
def checkout(request):
    if request.method == "POST":
        cart = request.session.get('cart', [])
        total = 0
        for item in cart:
            item['subtotal'] = item['price'] * item['quantity']
            total += item['subtotal']

        invoice = {
            'id': random.randint(1, 9999),
            'customer_name': request.POST.get('fullname', request.user.username),
            'total_amount': total,
            'items': [],
        }

        for item in cart:
            invoice['items'].append({
                'name': item['name'],
                'price': item['subtotal'],
            })

        request.session['invoice'] = invoice
        return redirect('invoice')  # توجيه لصفحة الفاتورة بعد الدفع

    return render(request, 'checkout.html')



def get_api(request):
     api_url = 'https://fakestoreapi.com/products' 
     response = requests.get(api_url)
     if response.status_code == 200:
            data = response.json()
     else:
            data={"error":f"error: {response.status_code}"}
     print(data)
     template = loader.get_template('get_api.html')
     return render(request, 'get_api.html', {'api_data': data})

def invoice(request):
    invoice = request.session.get('invoice', None)
    if invoice:
        return render(request, 'invoice.html', {'invoice': invoice})
    else:
        return HttpResponse("No invoice found.")