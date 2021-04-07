from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from .models import Contact
from .models import Orders
from .models import OrderUpdate
from math import ceil
import json
# Create your views here.
#[products, range(1,nslides), nslides],
#[products, range(1,nslides),  nslides] 

def index(request):
    products = product.objects.all()
    allprods=[]
    catprods= product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod) 
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
    params={'allprods':allprods }
    return render(request, 'shop/index.html',params) 
def about(request): 
        return render(request, 'shop/about.html')
def contact(request):
        if request.method=="POST":
                name = request.POST.get('name','')
                email = request.POST.get('email','')
                phone = request.POST.get('number','')
                desc = request.POST.get('text','')
                contact = Contact(name=name, email=email, phone=phone, desc=desc)
                contact.save()
        return render(request, 'shop/contact.html') 


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '') 
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update: 
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response) 
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')



def search(request): 
        render(request, 'shop/search.html')
def prodview(request, id):
        #fetch the product using the id
        Product = product.objects.filter(id=id) 
        print(Product)
        return render(request, 'shop/prodview.html',{'Product':Product[0]})
def checkout(request):
        thank=False
        ids=0
        if request.method=="POST":
            items_json = request.POST.get('itemsjson','')
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            phone = request.POST.get('phone','')
            address =request.POST.get('address1','') + " " + request.POST.get('adderss2',' ')
            city = request.POST.get('city', '')
            state  = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code','')
            order = Orders(name=name, email=email, phone=phone,address=address,city=city,state=state, zip_code=zip_code, items_json=items_json)
            order.save()
            update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed")
            update.save()
            thank=True
            ids = order.order_id;
        return render(request, 'shop/checkout.html', {'thanks':thank ,'id':ids} )
