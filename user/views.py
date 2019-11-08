from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUp
from django.core.mail import send_mail
from massage import settings
import uuid
from .models import Profile
from django.template.loader import render_to_string
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'GET':
        form = SignUp()
        return render(request, 'user/signup.html', {'form': form})

    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()

            verify_id = uuid.uuid4()
            profile = Profile(user=user, verify_id=verify_id)
            profile.save()

            email_host = settings.EMAIL_HOST
            email_user = settings.EMAIL_HOST_USER
            massage = render_to_string('user/verify.html', {'verify_id': verify_id})
            send_mail('verify', massage, email_host, [email_user])
        return HttpResponse('please check your email')


def verify(request, uid):
    user = Profile.objects.get(verify_id=uid)
    if user:
        user.verify = 1
        user.save()
        return redirect('login')


def listofuser(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'user/userslist.html', {'users': users})
    else:
        return redirect('login')
