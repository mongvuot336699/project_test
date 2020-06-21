from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Product
from .form import Product_form 


# Create your views here.
# show tat ca san pham
def show(request):
    items = Product.objects.all()
    return render(request,"show.html",{'items':items})

# them san pham
def creat(request):
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            return HttpResponse('Fail')
    else:
        form = Product_form()
    
    return render(request,'creat.html',{'form':form})

# cap nhat san pham
def update(request,id):
    product = Product.objects.get(id=id)
    form_update = Product_form(request.POST,request.FILES, instance= product)
    if form_update.is_valid():
        form_update.save()
        return redirect('show')
    return render(request,'update.html',{'product':product,'form_update':form_update})    

# xoa san pham
def delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('show')

# search san pham
def search(request):
    query = request.GET.get('query')
    
    result = Product.objects.filter(name__contains=query)
    if result != None:
        return render(request,'search.html',{'result':result})
    else:
        return HttpResponse("khong co san pham can tim")
        
    