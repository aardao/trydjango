from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form":form}
    return render(request,"accounts/register.html",context)

def login_view(request):
    # una forma para que no logees a un usuario que ya está logeado
    # if request.user.is_authenticated:
    #     return render(request,"acounts/already-logged-in.html",{})
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        #print(username, password)
        user = authenticate(request,username=username, password=password)
        login(request,user)
        if user is None:
            context = {"error": "Invalid username or password"}       
            return render(request,'accounts/login.html',context)
        return redirect('/')
    return render(request,'accounts/login.html',{})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect("/login/")
    return render(request,'accounts/logout.html',{})


