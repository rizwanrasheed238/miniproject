from itertools import product
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from cart.models import Cart, Whishlist
from category.models import Catagory, Product, Subcategory


#Add to Cart.
@login_required(login_url='login')
def addcart(request,id):
      user = request.user
      item=Product.objects.get(id=id) 
      if item.stock>0:
            if Cart.objects.filter(user_id=user,product_id=item).exists():
                  return redirect(cart)
            else:
                  product_qty=1
                  price=item.selling_price * product_qty
                  new_cart=Cart(user_id=user.id,product_id=item.id,product_qty=product_qty,price=price)
                  new_cart.save()
                  return redirect(cart)



# Cart Quentity Plus Settings
def plusqty(request,id):
    cart=Cart.objects.filter(id=id) 
    for cart in cart:   
        if cart.product.stock > cart.product_qty:
            cart.product_qty +=1
            cart.price=cart.product_qty * cart.product.selling_price
            cart.save()
            return redirect('cart')
        # messages.success(request, 'Out of Stock')
        return redirect('cart')

# Cart Quentity Plus Settings
def minusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product_qty > 1 :
            cart.product_qty -=1
            cart.price=cart.product_qty * cart.product.selling_price
            cart.save()
            return redirect('cart')
        return redirect('cart')
    

     
# View Cart Page
@login_required(login_url='login')
def cart(request):
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    total=0
    for i in cart:
        total += i.product.selling_price * i.product_qty
    category=Catagory.objects.all()
    subcategory=Subcategory.objects.all()
    return render(request,'cart.html',{'cart':cart,'total':total,'category':category,'subcategory':subcategory})

# Remove Items From Cart
def de_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)



#wishlist
@login_required(login_url='login')
def view_wishlist(request):  
    user = request.user
    wlist=Whishlist.objects.filter(user_id=user.id)
    print("zsxdcfvgbhnjm",wlist)
    return render(request,"wishlist.html",{'wlist':wlist})


@login_required(login_url='login')
def add_wishlist(request,id):
    item=Product.objects.get(id=id)
    user = request.user     
    if Whishlist.objects.filter( user_id =user.id,product_id=item.id).exists():
        return redirect('view_wishlist')        
    else:
        new_wishlist=Whishlist(user_id=user.id,product_id=item.id)
        new_wishlist.save()
        return redirect('view_wishlist')
    messages.success(request, 'Sign in..!!')
    return redirect(login)    


@login_required(login_url='login')
def de_wishlist(request,id):
    Whishlist.objects.get(id=id).delete()
    return redirect('view_wishlist')    