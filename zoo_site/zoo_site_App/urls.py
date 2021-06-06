from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('',views.animals,name='animals'),
    path('',views.tickets,name='tickets'),
    path('',views.thankyou,name='thankyou'),
    path('',views.instructions,name='instructions'),
]
