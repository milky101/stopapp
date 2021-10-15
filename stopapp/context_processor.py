from .models import ShopCart, Category


def cartread(request):
    cart = ShopCart.objects.filter(user__username=request.user.username, paid_order=False)

    cartreader = 0
    for item in cart:
        cartreader += item.quantity


    context = {
        'cartreader':cartreader
    }

    return context


def dropdown(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }

    return context