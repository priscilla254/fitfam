
from django.contrib.auth.decorators import login_required
from .models import  Plans,book
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from gym.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookForm
from .filters import bookFilter

class PlansList(LoginRequiredMixin,ListView):
    model=Plans
    context_object_name='plans'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
       # context['plans']=context['plans'].filter(user=self.request.user)
        context['count']=context['plans'].filter(complete=False).count()
        return context

class PlansDetail(LoginRequiredMixin,DetailView):
    model=Plans
    context_object_name='plans'
    template_name='planner/plan.html'

class PlansCreate(LoginRequiredMixin,CreateView):
    model=Plans
    fields='__all__'
    success_url=reverse_lazy('plans_list')

"""""
    def form_valid(self,form):
        
        form.instance.user=self.request.userprofile.user
        return super(PlansCreate,self).form_valid(form)
"""

class PlansUpdate(LoginRequiredMixin,UpdateView):
    model=Plans
    fields= '__all__'
    success_url=reverse_lazy('plans_list')

class PlansDelete(LoginRequiredMixin,DeleteView):
    model=Plans
    context_object_name='plan'
    success_url=reverse_lazy('plans_list')

@login_required(login_url='login')
def CreateBook(request):
    form=BookForm()
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_confirm')
    context={'form':form}
    return render(request,'planner/book.html',context)



def confirm_view(request):
    context={}
    return render(request,'planner/book_confirm.html',context)


def View_Bookings(request):
    bookings=book.objects.all().order_by('day','workout')
    myFilter=bookFilter(request.GET,queryset=bookings)
    bookings=myFilter.qs
    context={'bookings':bookings,'myFilter':myFilter}
    return render(request,'planner/bookings.html',context)

