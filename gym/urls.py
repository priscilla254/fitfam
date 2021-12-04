from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.index,name="home"),
    path('register/',views.RegisterView,name="register"),
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
    path('members/',views.MemberView,name="members"),
    path('create_member/',views.CreateMember,name="create_member"),
    path('contact/',views.ContactView,name="contact"),
    path('services/',views.ServicesView,name="services"),
    path('update_member/<int:pk>',views.UpdateMember,name="update_member"),
    path('delete_member/<int:pk>/',views.DeleteMember,name="delete_member"),
    path('user_profile/',views.UserProfileView,name="user_profile"),
    path('edit_profile/',views.editProfileView, name="edit_profile"),
    path('dashboard/',views.Dashboard_view,name="dashboard"),
    #password reset functionality
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='gym/password_reset.html'),
    name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='gym/password_reset_sent.html'),
    name="password_reset_done"),

    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='gym/password_reset_form.html'),
    name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='gym/password_reset_done.html'),
    name="password_reset_complete"),
]