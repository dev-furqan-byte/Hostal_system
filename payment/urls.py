
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("add_payment/", views.add_payment, name="add_payment"),
    path("payments/", views.payment_list, name="payment_list"),
    path("edit_payment/<int:id>/", views.edit_payment, name="edit_payment"),
    path("delete_payment/<int:id>/", views.delete_payment, name="delete_payment"),
    path("delete_payment/<int:id>/", views.delete_payment, name="delete_payment"),
]
