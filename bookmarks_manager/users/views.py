from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Login form
def login_view(request):
    if request.user.is_authenticated:
        return redirect('bookmark_list')  # If the user is already logged in, redirect to the homepage

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('bookmark_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Registration form
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Logout function
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

# API for login
@api_view(['POST'])
def api_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# API for registration
@api_view(['POST'])
def api_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Registration failed'}, status=status.HTTP_400_BAD_REQUEST)

# API for logout
@api_view(['POST'])
def api_logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

# Homepage after login
def home(request):
    return render(request, 'users/home.html')
