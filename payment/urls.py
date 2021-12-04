from django.urls import path
from .import views


urlpatterns = [
    path('subscriptions/',views.Plan_view,name="subscriptions"),
    #path('paymentredirect/',views.paymentview,name="paymentredirect"),
    path('paymentredirect/',views.charge,name="paymentredirect"),
    path('success/',views.successMsg,name="success")
]
