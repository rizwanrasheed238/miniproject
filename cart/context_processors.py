from cart.models import Cart


def counter(request):
    cart_count = 0
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
    else:
        carts = Cart.objects.all()
    for cart in carts:
        cart_count += cart.product_qty     
    return dict(cart_count=cart_count)