from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate as auth_authenticate,\
    login as auth_login

__all__ = [
    'login',
]

def login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('username/password is needed')
        user = auth_authenticate(
            email=email,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'login success')
            return redirect(next)
        else:
            messages.error(request, 'failed to login')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})