from itertools import product
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q


# def register(request):
#     return render(request,"register.html")
# def login(request):
#     return render(request,"login.html")
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account
#email verification import files
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from category.models import Catagory,Subcategory,Product
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    category=Catagory.objects.all()
    subcategory=Subcategory.objects.all()
    product=Product.objects.all()

    return render(request,"home.html",{'category':category,'subcategory':subcategory,'product':product})


# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         email=request.POST['email']
#         password=request.POST['password']
#         user=authenticate(email=email, password=password)
#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'you are logged in')
#             # request.session['email']=email
#             # request.session['fname']=user.fname
#             # # store user details in session
#             # request.session['district']=user.district
#             return redirect('home')
#         else:
#             print("demo")
#             messages.error(request, 'invalid login credentials')
#             return redirect('login')
#     return render(request, 'login.html')
# def register(request):
#     if request.method == 'POST':
#         email=request.POST['email']
#         password=request.POST['password']
#         lname = request.POST['lname']
#         fname=request.POST['fname']

#         phone_number=request.POST['phone_number']
#         print(email,password,fname,lname,phone_number)
#         if Account.objects.filter(email=email).exists():
#             messages.error(request, 'email already exists')
#             return redirect('register')
#         # elif Account.objects.filter(fname=fname).exists():
#         #     messages.error(request, 'username already exists')
#         #     return redirect('register')
#         else:
#             user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname, phone_number=phone_number)
#             user.save()
#             messages.success(request, 'you are registered')
#             return redirect('home')
#     return render(request, 'register.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('home')


def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            # request.session['email']=email
            # request.session['fname']=user.fname
            # # store user details in session
            # request.session['district']=user.district
            return redirect('home')
        else:
            print("demo")
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        lname = request.POST['lname']
        fname=request.POST['fname']

        phone_number=request.POST['phone_number']
        print(email,password,fname,lname,phone_number)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname, phone_number=phone_number)
            user.save()
            messages.success(request, 'Thank you for registering with us.')
            messages.success(request, 'Please verify your email for login!')

            current_site = get_current_site(request)
            message = render_to_string('account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'sparestore07@gmail.com',
                [email],
                fail_silently=False,
            )

            return redirect('/login/?command=verification&email=' + email)
            # return redirect('login')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# email varification

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


def profile(request):
    
    user=Account.objects.all()
    return render(request,"profile.html",{'user':user})

def singleproduct(request,id):
    product=Product.objects.filter(id=id)
    return render(request, "singleproduct.html",{'product':product})





    
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(name__icontains=query) | Q( description__icontains=query))
            products = Product.objects.filter(multiple_q) 
            return render(request, 'searchbar.html', {'product':products})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {})



def shop(request):
    category=Catagory.objects.all()
    subcategory=Subcategory.objects.all()
    product=Product.objects.all()

    return render(request,"shop.html",{'category':category,'subcategory':subcategory,'product':product})