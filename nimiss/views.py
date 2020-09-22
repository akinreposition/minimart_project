from django.shortcuts import render


# Create your views here.

def retail_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    my_context = {
        "name": "request.user",
        "phone": "Retail.phone",
    }
    return render(request, "index.html", {})


def cart_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    cart_list = {
        "is_cart_full": True,
        "number": 123456,
        "cart_names": ["cart1", "cart2", "cart3", "cart5", 'cart6', 000]
    }
    return render(request, "cart.html", cart_list)
