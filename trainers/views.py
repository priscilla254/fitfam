from django.shortcuts import render,redirect
from .models import*
from .filters import TrainerFilter
from gym.decorators import allowed_users
from .forms import*
@allowed_users(allowed_roles=['admins'])
def TrainerView(request):
    trainer=Trainer.objects.all().order_by('name')
    myFilter=TrainerFilter(queryset=trainer)
    trainer=myFilter.qs
    context={'trainer':trainer,'myFilter':myFilter}
    return render(request,'trainers/trainers_list.html',context)


def CreateTrainer(request):
    form=TrainerForm()
    if request.method=='POST':
        form=TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
    context={'form':form}
    return render(request,'trainers/trainer_form.html',context)

def UpdateTrainer(request,trainer_id):
    trainer=Trainer.objects.get(pk=trainer_id)
    form=TrainerForm(request.POST or None,instance=trainer)
    if form.is_valid():
        form.save()
        return redirect('trainers_list')
    context={'form':form,'trainer':trainer}
    return render(request,'trainers/trainer_form.html',context)

def DeleteTrainer(request,pk):
    trainer=Trainer.objects.get(id=pk)
    if request.method=='POST':
        trainer.delete()
        return redirect('trainers_list')
    context={'trainer':trainer}
    return render(request,'trainers/delete.html',context)