from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentModel

def login_view(request):
    usr="teacher"
    pwd="12345"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username==usr and password==pwd:
            return redirect('home') # Redirect to home page after login
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})

def home(request):
	data = StudentModel.objects.all()
	return render(request,"home.html",{"data":data})

def create(request):
	if request.method == "POST":
		data = StudentForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "record created"
			fm  = StudentForm()
			return render(request,"create.html",{"fm":fm,"msg":msg})
		else:
			msg = "check errors"
			return render(request,"create.html",{"fm":data,"msg":msg})
	else:
		fm = StudentForm()
		return render(request,"create.html",{"fm":fm})
