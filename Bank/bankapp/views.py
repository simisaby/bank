from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
from bankapp.models import RegForm


def home(request):
    return render(request,'home.html')


def login(request):
        if request.user.is_authenticated:
            return render(request,'user.html')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request,'user.html')
            else:
                messages.info(request, "Invalid credentials")
                return render(request, 'login.html')

        return render(request, 'login.html')


def logout(request):
        auth.logout(request)
        return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username,password=password)

                user.save()

                return render(request, 'register.html')
        else:
            messages.info(request, "password is not matched")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def user(request):
    return render(request,'user.html')
def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age =  request.POST['age']
        gender = request.POST['gender']
        phoneNumber =  request.POST['phoneNumber']
        email = request.POST['email']
        address =  request.POST['address']
        district =  request.POST['district']
        branch =  request.POST['branch']
        account = request.POST['account']
        materials = request.POST['materials']

        reg = RegForm.objects.create(name=name,dob=dob,age=age,gender=gender,phone=phoneNumber,email=email,address=address,
                               district=district,branch=branch,account_type=account,mater_provi=materials)
        reg.save()
        auth.logout(request)
        return render(request,'submittion.html')
    return render(request,'form.html')