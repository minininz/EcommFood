from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView,DetailView
from . models import Products,OrderPdts,Order
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

def checkout(request):
    order=Order()
    return render(request,'checkout.html',{'order':order})  

def placeorder(request):
    order_qs=Order.objects.filter(ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        
        for orderpdt in order.pdt.all():
            orderpdt.ordered=True
            orderpdt.save()
        order.ordered=True
        order.save()   
        
        messages.success(request,"Order placed Successfully!")
    else:
        messages.info(request,"No Order to Place")
    return render(request,'cart.html')

def fruit(request):
    
    pdts= Products.objects.filter(typee='Fruit')
    return render(request,'pdtfdisplay.html',{'pdts':pdts})
    
def veggie(request):
    pdts=Products.objects.filter(typee='Vegetable')
    return render(request,'pdtvdisplay.html',{'pdts':pdts})

def snack(request):
    pdts=Products.objects.filter(typee='Snack')
    return render(request,'pdtsdisplay.html',{'pdts':pdts})

def offer(request):
    pdts=Products.objects.filter(offer=True)
    return render(request,'pdtofferdisplay.html',{'pdts':pdts})

def addtocart(request):
    #qty=int(request.POST.get('qty'))
    name=request.POST.get('pdtname')
    pdt= get_object_or_404(Products,name= name)
    pdt_id=pdt.id
    orderpdt, created = OrderPdts.objects.get_or_create(pdt=pdt,ordered=False)
    order_qs=Order.objects.filter(ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        # for checking if item is already in order
        if order.pdt.filter(pdt_id=pdt_id).exists():
            orderpdt.qty= int(orderpdt.qty)+1
            orderpdt.save()
            messages.info(request, "Product quantity updated in Cart")
        else:
            messages.info(request, "Product added to Cart")
            order.pdt.add(orderpdt)
    else:
        ordered_date=timezone.now()
        order = Order.objects.create(ordered_date=ordered_date)
        order.pdt.add(orderpdt)
        messages.info(request, "Product added to Cart")
    link=request.POST.get('link','/')
    return redirect(link)

def removefromcart(request):
    name=request.POST.get('pdtname')
    pdt= get_object_or_404(Products,name= name)
    pdt_id=pdt.id
    order_qs=Order.objects.filter(ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        # for checking if item is already in order
        if order.pdt.filter(pdt_id=pdt_id).exists():
            orderpdt=OrderPdts.objects.filter(pdt=pdt,ordered=False)[0]
            
            if orderpdt.qty > 1:
                orderpdt.qty=int(orderpdt.qty)-1
                orderpdt.save()
                messages.info(request, "Product quantity updated in Cart")
            else:
                 order.pdt.remove(orderpdt)
                 orderpdt.delete()
                 messages.info(request, "Product removed from Cart")
           
            
        else:
            messages.info(request, "Product wasn't in your Cart")
            link=request.POST.get('link','/')
            return redirect(link)
    else:
        messages.info(request, "Product wasn't in your Cart")
        link=request.POST.get('link','/')
        return redirect(link)
    link=request.POST.get('link','/')
    return redirect(link)

def removetotal(request):
    name=request.POST.get('pdtname')
    pdt= get_object_or_404(Products,name= name)
    pdt_id=pdt.id
    order_qs=Order.objects.filter(ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        # for checking if item is already in order
        if order.pdt.filter(pdt_id=pdt_id).exists():
            orderpdt=OrderPdts.objects.filter(pdt=pdt,ordered=False)[0]
            order.pdt.remove(orderpdt)
            orderpdt.delete()
            messages.info(request, "Product removed from Cart")
           
            
        else:
            messages.info(request, "Product wasn't in your Cart")
            link=request.POST.get('link','/')
            return redirect(link)
    else:
        messages.info(request, "Product wasn't in your Cart")
        link=request.POST.get('link','/')
        return redirect(link)
    link=request.POST.get('link','/')
    return redirect(link)


