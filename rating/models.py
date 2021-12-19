from django.db import models
from datetime import datetime

class countries_info(models.Model):
    list_id=models.CharField(max_length=10)
    Entity_key=models.CharField(max_length=10)
        def __str__(self):
            return "%s " % (self.Entity_key)
            
class customer_info(models.Model):
    customer_key=models.CharField(max_length=100)
    residential_country_cd=models.ForeignKey('countries_info',null=True,on_delete=models.CASCADE)
    party_open_date=models.DateField()
    def __str__(self):
        return "%s " % (self.customer_key)

class customer_account_info(models.Model):
    account_key=models.CharField(max_length=100)
    primary_party_key=models.ForeignKey('customer_info',null=True,on_delete=models.CASCADE)
    acct_open_date=models.DateField()
    def __str__(self):
        return "%s" % (self.account_key)

class customer_transactions(models.Model):
    Transfer_key=models.CharField(max_length=100)
    account_key=models.ForeignKey('customer_account_info',null=True,on_delete=models.CASCADE)
    Transaction_Amount=models.IntegerField()
    Transcation_Origin=models.CharField(max_length=10)
    Transaction_date=models.DateTimeField()
    





