
from django.contrib import admin
from django.urls import path, include
from events import views
from events.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('events.urls'))
    
]
