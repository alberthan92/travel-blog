from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect

__all__ = [
    'logout',
]

def logout(request):
    auth_logout(request)
    messages.info(request, 'successfully logged-out')
    return redirect('front:intro')