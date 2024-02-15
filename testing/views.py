from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        Pass = request.POST.get('password')

        user = authenticate(request, username=username,password=Pass)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return render(request, 'main/index.html')

    return render(request, 'main/index.html')


def logout_user(request):
    logout(request)
    request.session.flush()  # Clear the session
    return redirect('index')



def reg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        Pass = request.POST.get('pass')

        my_user = User.objects.create_user(username=email,email=email,password=Pass)
        my_user.save()

        newReg = UserReg(
            user=my_user,
            email=email,
            name=name,
            phone=phone,
            addr=addr
        )

        newReg.save()
        return redirect('index')
    return render(request, 'main/reg.html')


def profile(request):
    user_id = request.user
    data = UserReg.objects.get(user=user_id)
    show = UserReg.objects.all()
    user_count = UserReg.objects.all().count()
    # user_count = UserReg.objects.filter(user=request.user.id).count()
    return render(request, 'main/profile.html', {'data': data, 'show':show, 'user_count':user_count})


def editprofile(request,id):
    user_id = request.user
    data = UserReg.objects.get(user=user_id)
    if request.POST:
        editName = request.POST.get('name')
        editEmail = request.POST.get('email')
        editPhone = request.POST.get('phone')
        editAddr = request.POST.get('addr')
        print(editName)
        data.name=editName
        data.email=editEmail
        data.phone=editPhone
        data.addr=editAddr
        data.save()
        return redirect('profile')
    return render(request,'main/editprofile.html',context={'data':data})


def deleteuser(request,id):
    deldata = UserReg.objects.get(user=id)
    deldata.delete()
    return redirect('index')
