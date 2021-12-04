from django.urls import path
from .views import  PlansCreate, PlansDelete, PlansDetail, PlansList, PlansCreate,PlansUpdate,PlansDelete

from .import views
urlpatterns=[
    path('plans_list/',PlansList.as_view(),name='plans_list'),
    path('plan/<int:pk>/',PlansDetail.as_view(),name="plan"),
    path('plans_form/',PlansCreate.as_view(),name="plans_form"),
    path('plans-update/<int:pk>/',PlansUpdate.as_view(),name="plans-update"),
    path('plans-delete/<int:pk>/',PlansDelete.as_view(),name="plans-delete"),
    path('book/',views.CreateBook,name="book"),
    path('book_confirm/',views.confirm_view,name="book_confirm"),
    path('bookings/',views.View_Bookings,name="bookings"),
   
    
]