from django.db import models

# Create your models here.
# Bank Model


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('pu', 'Public'), ('pr', 'Private'), ('co', 'Co-Operative')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " - " + self.location

# Customer Model


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    acc_type = models.CharField(max_length=50, choices=(
        ('sl', 'Salary'),
        ('sv', 'Savings'),
        ('jt', 'Joint')
    ))
    balance = models.IntegerField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
