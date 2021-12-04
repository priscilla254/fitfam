from gym.decorators import unauthenticated_user
from django.shortcuts import render,redirect

from .models import*
from trainers.models import Trainer
from django.core.mail import send_mail
from .filters import MemberFilter
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#forms
from .forms import MemberForm,CreateUserForm,ProfileForm
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user,allowed_users
import os
def index(request):
    return render(request,'gym/index.html')


@allowed_users(allowed_roles=['admins'])
def MemberView(request):
    member=Member.objects.all().order_by('status')
    myFilter=MemberFilter(request.GET,queryset=member)
    member=myFilter.qs
    context={'member':member,'myFilter':myFilter}
    return render(request,'gym/members.html',context)

#CRUD operations
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def CreateMember(request):
    form=MemberForm()
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
    context={'form':form}
    return render(request,'gym/member_form.html',context)

    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def UpdateMember(request,pk):
    member=Member.objects.get(id=pk)
    form= MemberForm(instance=member)
    if request.method=="POST":
        form=MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    context={'form':form}
    return render(request,"gym/member_form.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def DeleteMember(request,pk):
    member=Member.objects.get(id=pk)
    if request.method=="POST":
        member.delete()
        return redirect('members')
    context={'member':member}
    return render(request,'gym/delete.html',context)




def ContactView(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        send_mail(
            name, # subject
            subject, #message
            email,#from email
            [os.environ.get('EMAIL_HOST_USER')],
        )
        return render(request,'gym/contact.html',{'name':name})
    return render(request,'gym/contact.html')

def ServicesView(request):
    service=Services.objects.all()
    context={'service':service}
    return render(request,'gym/services.html',context)

# registration and login
@unauthenticated_user
def RegisterView(request):
    form =CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customers')
            user.groups.add(group)
            UserProfile.objects.create(
                user=user
            )

            messages.success(request,'account was created for '+username)
            return redirect('login')
    context={'form':form}
    return render(request,'gym/register.html',context)

@unauthenticated_user
def LoginView(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username OR Password is incorrect")
        
    context={}
    return render(request,'gym/login.html',context)

def LogoutView(request):
    logout(request)
    messages.info(request,"you have successfully logged out.")
    return redirect('/')

#user profile page
@login_required(login_url='login')
@allowed_users(allowed_roles=['customers','admins'])
def UserProfileView(request):
    member=request.user.userprofile
    form= MemberForm(instance=Member)
    member=Member.objects.all()
    if request.method=='POST':
        form=MemberForm(request.POST,request.FILES,instance=Member)
        if form.is_valid():
            form.save()
            return redirect('user')
    context={'form':form,'member':member}
    return render(request,'gym/user_profile.html',context)

def editProfileView(request):
    member=request.user.userprofile
    form=ProfileForm(instance=member)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=member)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    context={'form':form}
    return render(request,'gym/edit_profile.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def Dashboard_view(request):
    total_members=Member.objects.count()
    total_trainers=Trainer.objects.count()
    context={'total_members':total_members,'total_trainers':total_trainers}
    return render(request,'gym/dashboard.html',context)