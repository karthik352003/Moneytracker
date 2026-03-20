from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    
    )
    CATEGORY_CHOICES = (
    ('food', 'Food'),
    ('transport', 'Transport'),
    ('shopping', 'Shopping'),
    ('bills', 'Bills'),
    )


    date = models.DateField()
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.amount}"

class New_user (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    transaction =models.ForeignKey(Transaction,on_delete=models.CASCADE)
    