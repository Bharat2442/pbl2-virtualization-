from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"

class Budget(models.Model):
    total_budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Budget: ₹{self.total_budget}"
