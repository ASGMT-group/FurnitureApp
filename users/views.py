
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User
from baseapp.models import cart
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # Replace 'home' with the name of your home view
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    return render(request, 'login.html')




User = get_user_model()



def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # Check if the user already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'A user with the same username or email already exists.')
                return render(request, 'signup.html', {'form': form})
            
            # Create the new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            user_cart = cart.objects.create(cart_owner=user)
            user_cart.save()
            # Authenticate and login the user
            
            return redirect('login')
            
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    return render(request,'profile.html')



def logou_user(request):
    if request.user.is_authenticated and not isinstance(request.user, AnonymousUser):
        logout(request)
    return redirect('login')