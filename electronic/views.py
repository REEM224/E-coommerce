from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import product
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .forms import ProductForm
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Create your views here.
def list_electronic(request):
    electronic=[
         {'id': 1, 'name': 'labtop Dell 14 inspiron', 'price': 3700,
     'description': 'labtop Dell 14 inspiron 5000 series',
     'image': 'https://i.pinimg.com/474x/52/bf/84/52bf84a5cf2bd4db43c93a83607fbddf.jpg'},

    {'id': 2, 'name': 'labtop HP 15', 'price': 4000,
     'description': 'labtop HP 15 3000 series',
     'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8'},

    {'id': 3, 'name': 'labtop Acer Aspire 3', 'price': 3500,
     'description': 'labtop Acer Aspire 3 3000 series',
     'image': 'https://m.media-amazon.com/images/I/71vvXGmdKWL._AC_SL1500_.jpg'},

    {'id': 4, 'name': 'labtop Lenovo IdeaPad 3', 'price': 3800,
     'description': 'labtop Lenovo IdeaPad 3 3000 series',
     'image': 'https://i.pinimg.com/736x/23/87/c1/2387c1176ca0ca230af39bf387b33bbf.jpg'},

    {'id': 5, 'name': 'labtop Asus VivoBook 15', 'price': 3900,
     'description': 'labtop Asus VivoBook 15 3000 series',
     'image': 'https://i.pinimg.com/736x/48/9a/cf/489acf8496021b002f61931069525622.jpg'}
    ]
    context={
        'lol':electronic
        
        }
    #print(request)لتتحقق من مرور البيانات 
    tamplate=loader.get_template('list_electronic.html')
    return HttpResponse(tamplate.render(context))




def showphone(request, phone):
    template = loader.get_template('phone.html')
    value = {
        'ph': phone,
    }
    print(phone)
    return HttpResponse(template.render(value, request))

# @csrf_exempt
# def showcategories(request):
#     template = loader.get_template('categories.html')  
#     x = request.POST.get('title')
#     y = request.POST.get('address')
#     print(x)
#     print(y)
#     value = {
#         'title': x,
#         'address': y
#     }
#     return HttpResponse(template.render(value))

# def product(request):
#     prd = product.objects.all()
#     print(prd)





@csrf_exempt  
def showcategories(request):  # جعل val اختياريًا
    val=request.GET.get('val')
    print(val)
    if  not val :
        products = product.objects.all()
    else:
        products = product.objects.filter(name=val) .values() 
      
     
    tamplate = loader.get_template('categories1.html')
    form = ProductForm()
    forms={
        'form':form,
        'prd':products
    }
    return HttpResponse(tamplate.render(forms))

#pring data from user to the store in database

@csrf_exempt
def create(request):
   name=request.POST.get('name')
   color=request.POST.get('color')
   price=request.POST.get('price')
   quintity=request.POST.get('quintity')
   tax=request.POST.get('tax')
   total=request.POST.get('total')
   date=request.POST.get('date')
   net=request.POST.get('net')
   prod=product(name=name,color=color,price=price,quintity=quintity,tax=tax,total=total,date=date,net=net)
   prod.save()
   #return HttpResponse('ok')
   return redirect('/showcategories/')
   



#def delete(request, product_id):

    #prd = get_object_or_404(product, id=product_id)
    #prd.delete()
    #return redirect('showcategories')
def delete(request, product_id):
    if request.method == "GET":
        try:
            prd = get_object_or_404(product, id=product_id)
            prd.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
        


def edit(request, product_id):
    tamplate = loader.get_template('edit1.html')
    prd = get_object_or_404(product, id=product_id)
    items = {
        'product': prd,
    }
    return HttpResponse(tamplate.render(items, request))

@csrf_exempt
def update(request):
   id=request.POST.get('id')
   name=request.POST.get('name')
   color=request.POST.get('color')
   price=request.POST.get('price')
   quintity=request.POST.get('quintity')
   tax=request.POST.get('tax')
   total=request.POST.get('total')
   date=request.POST.get('date')
   net=request.POST.get('net')

   prd = product.objects.get(id=id)#get the object by id

   prd.name=name
   prd.color=color
   prd.price=price      
   prd.quintity=quintity
   prd.tax=tax
   prd.total=total
   prd.net=net

   prd.save()
   return redirect('showcategories')
   
   

def test (request):
   return HttpResponse(request.session['cart_count'])
   #print(name)
   

   #data={
        
      #   'name':name,
      #   'color':color,
       #  'price':price,
       #  'quintity':quintity,
        # 'tax':tax,
         #'total':total,
         #'date':date,
         #'net':net   
   #}
 
