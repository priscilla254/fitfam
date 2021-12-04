from django.urls import path
from . import views

urlpatterns=[
    path('trainers_list/',views.TrainerView,name="trainers_list"),
    path('create_trainer/',views.CreateTrainer,name="create_trainer"),
    path('update_trainer/<trainer_id>/',views.UpdateTrainer,name="update-trainer"),
    path('delete_trainer/<int:pk>',views.DeleteTrainer,name="delete_trainer"),
    ]