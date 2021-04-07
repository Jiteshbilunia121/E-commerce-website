from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "shophome"),
    path('about/',views.about, name = "aboutus"),
    path('contact/', views.contact, name = "contactus"),
    path('tracker/', views.tracker, name = "trackorder"),
    path('search/', views.search, name = "Search"),
    path('products/<int:id>', views.prodview, name = "productview"),
    path('checkout/', views.checkout, name = "checkout"),

]