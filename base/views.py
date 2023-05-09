from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student
from .forms import StudentForm
# Create your views here.

updatestatus=False

     
def home(request):
    
	# Check to see if logging in
	s=Student.objects.all()
	updatestatus=False 
	context={'data':s,'edit': updatestatus}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		# Authenticate
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
			
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
	    return render(request,'base/index.html',context)
	
def edit(request, id):
    s=Student.objects.all()
    d = Student.objects.get(id=id)
    form=StudentForm(instance=d)
    context = {'d': d,'data':s,'edit':True} 
    if request.method == "POST":
        form=StudentForm(request.POST,instance=d)
        if form.is_valid():
              form.save()
        return redirect('home')

    return render(request, 'base/edit.html', context)

def edit1(request, id):
    s=Student.objects.all()
    d = Student.objects.get(id=id)
    context = {'d': d,'data':s,'edit':True} 
    if request.method == "POST":
        fname = request.POST.get('fname')	
        lname = request.POST.get('lname')	
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
	
        d.first_name = fname
        d.last_name = lname
        d.email = email
        d.age = age
        d.gender = gender
        d.save()
        return redirect('home')

    return render(request, 'base/edit.html', context)


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # f = form.save()
         
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request,'base/index.html')



def add1(request):
         		
		if request.method == 'POST':    
			fname=request.POST['fname']
			lname=request.POST['lname']
			email=request.POST['email']
			age=request.POST['age']
			gender=request.POST['gender']
			s=Student()
			s.first_name=fname
			s.last_name=lname
			s.email=email
			s.age=age
			s.gender=gender
			s.save()
			return redirect('home')
		
		return render(request,'base/index.html')

def delete(request, id):
   d = Student.objects.get(id=id)
   context = {'d': d}
   if request.method == "POST":
        d.delete()
        return redirect('home')
   
   return render(request, 'base/delete.html', context)