from remote.models import Remote_bookings
from remote.forms import RemoteBookingForm
from django.shortcuts import render,redirect
from .forms import RemoteBookingForm


def RemoteView(request):
    remote_bookings=Remote_bookings.objects.all().order_by('date','time')
    context={'remote_bookings':remote_bookings}
    return render(request,'remote/remote_list.html',context)


def CreateRemoteBook(request):
    form=RemoteBookingForm()
    if request.method=='POST':
        form=RemoteBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remote_confirm')
    context={'form':form}
    return render(request,'remote/remote_bookings.html',context)

def RemoteConfirm_view(request):
    return render(request,'remote/remote_confirm.html')
