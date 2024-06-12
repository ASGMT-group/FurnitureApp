from django.shortcuts import render,get_object_or_404,redirect
from .models import furniture_item, cart
from datetime import date

def home(request):

    items = furniture_item.objects.all
    new_arr = furniture_item.objects.filter(date_created__date=date.today())

    featured = furniture_item.objects.filter(item_rating__gte=4)

    return render(request, "home.html", {"items":items, "new_item":new_arr,'featured':featured })



def collections(request):
        # Get the selected category from the request parameters
    selected_category = request.GET.get('category', '')

    # Get the search query from the request parameters
    search_query = request.GET.get('search_query', '')

    # Filter the FurnitureItem objects based on the selected category and search query
    if selected_category:
        items = furniture_item.objects.filter( item_type=selected_category.lower())
    else:
        items = furniture_item.objects.all()

    if search_query:
        items = items.filter(item_name__icontains=search_query)

    # Pass the filtered items, selected category, and search query to the template context
    context = {
        'items': items,
       
    }

    return render(request, "filter.html", context)



def rate_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(furniture_item, id=item_id)
        new_rating = float(request.POST['rating'])
        item.update_rating(new_rating, request.user)
        return redirect('detail', item_id=item.id)
    else:
        return render(request, 'rate_item.html', {'item_id': item_id})

def item_detail(request, item_id):
    item = get_object_or_404(furniture_item, id=item_id)
    
    rated_items = furniture_item.objects.filter(rated_by=request.user)
    is_rated = False
    if rated_items:
        is_rated = True

    return render(request, "item_detail.html", {"item":item,'is_rated':is_rated})

def add_to_cart(request, item_id):
  
    item = get_object_or_404(furniture_item, id=item_id)
    user_cart, created = cart.objects.get_or_create(cart_owner=request.user)
    user_cart.items.add(item)
    return redirect('home')
    


def display_cart(request):
    if request.user.is_authenticated:
        user_cart = cart.objects.get(cart_owner=request.user)
        cart_items = user_cart.items.all()
        total_price = 0

        for item in cart_items:
            total_price += item.item_price

        context = {
            'cart': cart_items,
            'total_price': total_price,
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('login')
def delete_item(request, item_id):
    if request.user.is_authenticated:
        user_cart = cart.objects.get(cart_owner=request.user)
        item = get_object_or_404(furniture_item, id=item_id)
        user_cart.items.remove(item)
        return redirect('cart')
    else:
        return redirect('login')
    

    