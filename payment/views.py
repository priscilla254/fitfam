from django.shortcuts import render,redirect
from stripe.api_resources import customer,charge
from .models import MemberPayment
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
import json
from django.http import JsonResponse
import stripe
import os
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

#stripe 
def charge(request):
    
    if request.method=='POST':
        print('Data:',request.POST)
        amount=int(request.POST['amount'])

        customer=stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['username'],
            source=request.POST['StripeToken'],
            )
     

        charge=stripe.Charge.create(
            customer='cus_K6LINZMsQAHic1',
            amount=amount*100,
            currency='usd',
            description="gym subscription"
        )
        
        return redirect(reverse('success'))
    return render(request,'payment/paymentredirect.html')


           
            
def successMsg(request):
    
    return render(request,'payment/success.html')

def Plan_view(request):
    plan=MemberPayment.objects.all()
    context={'plan':plan}
    return render(request,'payment/subscriptions.html',context)


def paymentview(request):
   return render(request,'payment/paymentredirect.html')


    
   

def MemberPaymentView(request):
    object=MemberPayment.objects.all()
    context={'object':object}
    return render(request,'Payment/member_payment.html',context)