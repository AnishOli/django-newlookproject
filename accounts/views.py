from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout,authenticate
from .forms import CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from accounts.models import Customer
from django.contrib.auth.hashers import check_password
import os

def register(request):
    if request.method == "POST":
       # receive payload setp1
    
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        city = request.POST.get("city")
        dob = request.POST.get("dob")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
 #step 2 validate 
        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Email exists check
        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            return redirect("register")

        # Phone exists check
        if Customer.objects.filter(phone_number=phone).exists():
            messages.error(request, "Phone number is already registered!")
            return redirect("register")

        

       # cretae db model

        # Create user
        user = Customer.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone,
            city=city,
            dob=dob,
            password=password1,
            
            
        )
        print(user)
        
        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "users/register.html")



def user_login(request):
    if request.method == "POST":
        #receive data
        #validation
        #check data exist on db
        # save login detail
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = Customer.objects.get(email= email)
        except Customer.DoesNotExist:
            messages.error(request,"user doesnot exist")
            return render(request, 'users/login.html')
        
        if check_password(password,user.password):
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Sorry incorrect password")
    return render(request, 'users/login.html')

    
    return render(request, "users/login.html")
    


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def user_home(request):
    return render(request, 'users/home.html')

@login_required
def user_profile(request):
    customer = request.user

    if request.method == "POST":
        customer.first_name = request.POST.get("first_name")
        customer.last_name = request.POST.get("last_name")
        customer.phone_number = request.POST.get("phone_number")
        customer.city = request.POST.get("city")

        dob_value = request.POST.get("dob")
        if dob_value == "" or dob_value is None:
            customer.dob = None
        else:
            customer.dob = dob_value

        customer.save()
        return redirect("profile")

    return render(request, 'users/profile.html', {'customer': customer})

@login_required
def update_profile_image(request):
    if request.method == "POST":
        image = request.FILES.get("profile_image")
        if image:
            request.user.profile_image = image
            request.user.save()
        return redirect("profile")
    



@login_required
def delete_profile_image(request):
    user = request.user
    
    # Only delete if not default
    if user.profile_image and user.profile_image.name != "profile1.jpg":
        image_path = user.profile_image.path
        
        if os.path.exists(image_path):
            os.remove(image_path)   # delete file from disk

    # Reset to default
    user.profile_image = "profile1.jpg"
    user.save()

    return redirect("profile")
