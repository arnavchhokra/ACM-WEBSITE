from django.urls import path
from . import views


urlpatterns = [
    path('events/',views.events_list,name="events-list"),
    path('events/<str:pk>/',views.events_detail, name="events-detail"),
  #  path('Bag/',views.orders_list),
   # path('hello/', views.HelloView.as_view(), name ='hello'),
   # path('Bag/<str:pk>/',views.orders_detail)
]
