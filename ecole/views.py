from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomerUser


def Base(request):
	return render(request,'base.html')


def Login(request):
	return render(request,'login.html')


def Dologin(request):
	if request.method == "POST":
		user = EmailBackend.authenticate(request,
			username=request.POST.get('email'),
			password=request.POST.get('password'),
			)
		if user!=None:
			login(request,user)
			user_type = user.user_type

			if user_type == '1':
				return redirect('homeadmin')

			elif user_type == '2':
				return redirect('home_staff')

			elif user_type == '3':
				return redirect('home_stud')

			else :
				messages.error(request, 'email ou mot de pass invalide')
				return redirect('login')
		else:
			messages.error(request, 'email ou mot de pass invalide')
			return redirect('login')

def Dologout(request):
	logout(request)
	return redirect('login')

@login_required(login_url='/')
def PRofile(request):
	user = CustomerUser.objects.get(id=request.user.id)

	context ={
	'user':user
	}
	return render(request,'profile.html',context)

@login_required(login_url='/')
def Profile_modif(request):
	if request.method == "POST":
		profile_img = request.FILES.get("profile_img")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		#email = request.POST.get("email")
		#username = request.POST.get("username")
		password = request.POST.get("password")

		try:
			customeruser = CustomerUser.objects.get(id=request.user.id)
			customeruser.first_name = first_name
			customeruser.last_name = last_name
			

			if password != None and password != "":
				customeruser.set_password(password)
			if profile_img != None and profile_img !="":
				customeruser.profile_pic = profile_img

			customeruser.save()
			messages.success(request,'votre profile a ete modifier avec succes')
			return redirect('profile')
			
		except:
			messages.error(request,'erreur , profil non modifier')

	return render(request,'profile.html')