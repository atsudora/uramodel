from django.db import IntegrityError

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザー名は既に登録されています。'})
    