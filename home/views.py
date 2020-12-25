from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Register,Product

# Create your views here.
def home(request):
    return render(request,'home/homepage.html')
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        message=""
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('products')
            else:
                message=messages.info(request,'Username Or Password is Incorrect')
        return render(request,'login/login.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        if request.method=="POST":
            f2=CreateUserForm(request.POST)
            print(f2)
            if f2.is_valid():
                user=f2.save()
                group=Group.objects.get(name='customer')
                user.groups.add(group)
                obj=Register(username=f2.cleaned_data['username'],fisrt_name=f2.cleaned_data['first_name'],last_name=f2.cleaned_data['last_name'],email=f2.cleaned_data['email'],phone=request.POST['phone'],address=request.POST['address'])
                obj.save()
                return redirect('login')
            else:
                print("some error")
        else:
            f2=CreateUserForm()
        context={'form':f2}
        return render(request,'signup/signup.html',context)


@login_required(login_url='login')
def products(request):
    return render(request,'products/imagespage.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def bakeware(request):
    obj=Product.objects.filter(name__contains='Bakeware:')
    context={'objs':obj}
    return render(request,'Bware/short_products.html',context)

def product_detail(request, pk_test ):
    obj=Product.objects.filter(name=pk_test)
    return render(request,'bakeware/itemSpecification.html',{'obj':obj})

@login_required(login_url='login')
def cart(request):
    return render(request,'cart/cart.html')
