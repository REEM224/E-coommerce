from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import product
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def list_beauty(request):
    beauty=[
        {'id':1,'name':'dior forever noude bronze','price':295,'description':'dior forever noude bronze 5000 series','image':'https://i.pinimg.com/474x/de/3e/9e/de3e9e6ea454a0cd912c46cdf6afba26.jpg'},
        {'id':2,'name':'dior forever hydra nude ','price':300,'description':'dior forever hydra nude 3000 series','image':'https://i.pinimg.com/736x/d3/b5/17/d3b51769a5b55805b64137663ec94f03.jpg'},
        {'id':3,'name':'dior forever matte','price':600,'description':'dior forever matte 3000 series','image':'https://i.pinimg.com/736x/2c/79/6f/2c796f218cdf365b26456a857ea18bba.jpg'},
        {'id':4,'name':'dior forever skin glow','price':500,'description':'dior forever skin glow 3000 series','image':'https://i.pinimg.com/736x/b7/7c/6c/b77c6c5069696ebd1384a9bdaac0f402.jpg'},
        {'id':5,'name':'dior forever skin correct','price':700,'description':'dior forever skin correct 3000 series','image':'https://i.pinimg.com/736x/38/be/e5/38bee5c4a32f621738ea8d4c78ecf17d.jpg'},
    ]
    context={
        'beauty1':beauty
        
        }
    #print(request)
    tamplate=loader.get_template('list_beauty.html')
    return HttpResponse(tamplate.render(context))

def showbeauty(request):
    tamplate=loader.get_template('pbeauty2.html')
    return HttpResponse(tamplate.render())

def product_list(request):
    tamplate=loader.get_template('product.html')
    prd=product.objects.all()
    #print(prd)
    value={
        'prodkey':prd
        
        }
    return HttpResponse(tamplate.render(value))

#@csrf_exempt  
#def showcategories(request):
#   products = product.objects.all()
#    print(products)
 #   tamplate = loader.get_template('categories.html')
  #  form = ProductForm()
  #  forms={
  #      'form':form,
  #      'product':products
  #  }
  #  return HttpResponse(tamplate.render(forms))


@csrf_exempt  
def showcategoriesBeauty(request):  # جعل val اختياريًا
    val=request.GET.get('val')
    print(val)
    if  not val :
        products = product.objects.all()
    else:
        products = product.objects.filter(name=val) .values() 
      
     
    tamplate = loader.get_template('categories.html')
    form = ProductForm()
    forms={
        'form':form,
        'prad':products
    }
    return HttpResponse(tamplate.render(forms))

#pring data from user to the store in database

@csrf_exempt
def create1(request):
   name=request.POST.get('name')
   color=request.POST.get('color')
   price=request.POST.get('price')
   quintity=request.POST.get('quintity')
   tax=request.POST.get('tax')
   total=request.POST.get('total')
   date=request.POST.get('date')
   net=request.POST.get('net')
   prad=product(name=name,color=color,price=price,quintity=quintity,tax=tax,total=total,date=date,net=net)
   prad.save()
   #return HttpResponse('ok')
   return redirect('showcategoriesBeauty') 




def delete1(request, product_id):
 
    prad = get_object_or_404(product, id=product_id)
    prad.delete()
    return redirect('showcategoriesBeauty')


def edit1(request, product_id):
    tamplate = loader.get_template('edit.html')
    prad = get_object_or_404(product, id=product_id)
    items = {
        'product': prad,
    }
    return HttpResponse(tamplate.render(items, request))


