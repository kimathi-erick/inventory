from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import reg,productform,profileupdate,userupdate,orderform
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    allproducts= Product.objects.all()
    orders_count= Order.objects.all().count()
    if request.method == 'POST':
        form=productform(request.POST)
        if form.is_valid():
            form.save()
            pname=form.cleaned_data.get('name')
            messages.success(request,f'{pname} has been added')
            return redirect('home')
    else:
        form=productform() 
    if request.method == 'POST':
        form=orderform(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('Orders')
    else:
        form=orderform()       
    context={

        'form':form,
        'form':form,
        'allproducts':allproducts,
        'orders_count':orders_count
    }    
    return render(request,'home.html',context)
@login_required(login_url='register')    
def Staff(request):
    workers=User.objects.all()
    context={
        'workers':workers
    }
    return render(request,'staff.html',context)
@login_required   
def Products(request):
    allproducts= Product.objects.all() 
    orders_count= Order.objects.all().count()
    if request.method == 'POST':
        form=productform(request.POST)
        if form.is_valid():
            form.save()
            pname=form.cleaned_data.get('name')
            messages.success(request,f'{pname} has been added')
            return redirect('home')
    else:
        form=productform()  
    context={
        'allproducts':allproducts,
        'form':form,
        'orders_count':orders_count
    }

    return render(request,'products.html',context)
@login_required  
def Orders(request):
    allorders= Order.objects.all()
    if request.method == 'POST':
        form=orderform(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('Orders')
    else:
        form=orderform()    
    context={
        'allorders':allorders,
        'form':form,
    }
    return render(request,'orders.html',context) 
def register(request):
    if request.method == 'POST':
        form=reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=reg()
    context={
        'form':form
    }
    return render(request,'register.html',context)           
def Profilepage(request):
    return render(request,'profile.html')

def productretrieve(request,pk):
    
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('home')
    context={
        'item':item
    }    
    return render(request,'retrieve.html',context)   
def productdelete(request,pk):
    
    item=Product.objects.get(id=pk)
    
    item.delete()
    return redirect('home')  
def productedit(request,pk):
    
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        
        form=productform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=productform(instance=item)        
    context={
        'form':form
    }        
    return render(request,'edit.html',context)   

def profile_update(request):
    if request.method == 'POST':
        user_form = userupdate(request.POST,instance=request.user)
        profile_form=profileupdate(request.POST,request.FILES,instance=request.user.profile) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save() and profile_form.save()
            return redirect('home') 
    else:
        user_form = userupdate(instance=request.user)
        profile_form=profileupdate(instance=request.user.profile) 
        
    context={
        'profile_form':profile_form,
        'user_form':user_form
    } 
    return render(request,'profileupdate.html',context)   
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            allproducts= Product.objects.filter(name__icontains=query)
            context={
                'allproducts':allproducts
            }
        else:
            print('product out of stock')
            context={}
    return render(request,'search.html',context)        


    


