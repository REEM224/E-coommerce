"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home import views as _home
from electronic import views as _electronic
from beauty import views as _beauty
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', _home.showland, name='showland'),
    path('electronic', _electronic.list_electronic,name='list_electronic'),
    path('showphone/<str:phone>/', _electronic.showphone, name='showphone'),
    path('beauty', _beauty.list_beauty,name='list_beauty'),
    path('showbeauty/', _beauty.showbeauty,name='showbeauty'),
    path('showcategories/', _electronic.showcategories, name='showcategories'),
    path('product/', _beauty.product_list, name='product_list'),
    path('showcategoriesBeauty/', _beauty.showcategoriesBeauty, name='showcategoriesBeauty'),
    path('create/', _electronic.create, name='create'),
    path('create1/', _beauty.create1, name='create1'),
    path('delete1/<int:product_id>/', _beauty.delete1, name='delete1'),
    path('delete/<int:product_id>/', _electronic.delete, name='delete'),
    path('edit1/<int:product_id>/', _beauty.edit1, name='edit1'),
    path('edit/<int:product_id>/', _electronic.edit, name='edit'),
    path('update/', _electronic.update, name='update'),
    path('list_products/<int:id>/', _home.list_products, name='list_products'),
    path('productdetails/<int:id>/', _home.productdetails, name='productdetails'),
    path('addtocart/', _home.add_to_cart, name='addtocart'),
    path('test/', _electronic.test, name='test'),
    path('checkout/', _home.checkout, name='checkout'),
    path('account/',include('account.urls')),  # Include account URLs
    path('get_api/', _home.get_api, name='get_api'),  # Include account URLs
    path('invoice/', _home.invoice, name='invoice'),  # Include account URLs



         
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)