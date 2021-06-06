from django.contrib import admin
from django.urls import path,include
from zoo_site_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('',include('zoo_site_App.urls')),
    path('animals/',views.animals,name='animals'),
    path('tickets/',views.tickets,name='tickets'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('instructions/',views.instructions,name='instructions'),


]
