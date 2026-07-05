from django.db import models
from django.utils import timezone


class Payment(models.Model):

    STATUS_CHOICES = [
        ("paid", "Paid"),
        ("unpaid", "Unpaid"),
    ]
    boy = models.ForeignKey(
        "hostal.Boy",
        on_delete=models.CASCADE,
        related_name="payments"
    )
    month = models.CharField(max_length=20)
    year = models.IntegerField(default=timezone.now().year)
    advance = models.PositiveIntegerField(default=0)
    rent = models.PositiveIntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="unpaid"
    )
    paid_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.boy.full_name} - {self.month} {self.year}"
    class Meta:
        unique_together=('boy','month','year')
