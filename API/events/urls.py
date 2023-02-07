from django.urls import path
from . import views


urlpatterns = [
    path('events/',views.events_list,name="events-list"),
    path('events/<str:pk>/',views.events_detail, name="events-detail"),
    path('events/register/',views.events_post,name="events-register")
]
