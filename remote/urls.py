from django.urls import path
from . import views
urlpatterns=[
    path('remote_bookings/',views.CreateRemoteBook,name="remote_bookings"),
    path('remote_confirm/',views.RemoteConfirm_view,name="remote_confirm"),
    path('remote_list/',views.RemoteView,name="remote_list")
    
]