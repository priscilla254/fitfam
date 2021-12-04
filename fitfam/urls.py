
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gym.urls')),
    path('',include('planner.urls')),
    path('',include('payment.urls')),
    path('',include('trainers.urls')),
    path('',include('remote.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
