from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import UserInfo

# Create your views here.

def user_register(request):
    if request.user.is_authenticated:
        return redirect('members')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userInfo_form = UserInfoForm(request.POST)

        if user_form.is_valid() and userInfo_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()
            
            userInfo = userInfo_form.save(commit=False)
            userInfo.user = user
            if 'profile_pic' in request.FILES:
                userInfo.profile_pic = request.FILES['profile_pic']

            userInfo.save()
            registered = True
            messages.success(request, "Account created successfully, you can now login🥳")
            return redirect('login')

    else:
        user_form = UserForm()
        userInfo_form = UserInfoForm()
    dict = {'user_form': user_form, 'userInfo_form': userInfo_form, 'registered': registered}

    return render(request, 'signup.html', context=dict)




def user_login(request):
    if request.user.is_authenticated:
        return redirect('members')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('members')
        else:
            messages.error(request, 'Aurhentication failed :( may not be logged in due to invalid username or password')
        

    return render(request, 'login.html')


@login_required
def member_page(request):
    users = UserInfo.objects.all()
    return render(request, 'members.html', {'users': users})



def user_logout(request):
    logout(request)
    return redirect('login')