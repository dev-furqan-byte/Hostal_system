from django.contrib import admin
from payment.models import Payment
# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("boy", "month", "year", "rent", "advance", "status")
    list_filter = ("status", "month", "year")
    search_fields = ("boy__full_name",)