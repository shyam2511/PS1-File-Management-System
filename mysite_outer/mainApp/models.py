from django.db import models


# Create your models here.

class Customer(models.Model):
    CustomerId = models.CharField(max_length=30, primary_key=True)  # changed floatfield to charfield
    EnterpriseName = models.CharField(max_length=50, null=True, blank=True)
    CustomerName = models.CharField(max_length=50)
    EmailId = models.EmailField(max_length=30, null=True, blank=True)
    MobileNumber = models.CharField(max_length=10, null=True, blank=True)
    Status = models.CharField(max_length=20, null=True, blank=True)
    ProfileComplete = models.CharField(max_length=5, null=True, blank=True)
    KYCStatus = models.CharField(max_length=20, null=True, blank=True)
    CustomerGroup = models.CharField(max_length=30, null=True, blank=True)
    CurrentLoyaltyPoints = models.FloatField()  # changed integer to float
    TotalLoyaltyPoints = models.FloatField()  # changed integer to float
    LastRedemption = models.FloatField()
    TotalRedemption = models.FloatField()
    BonusUponTotal = models.CharField(max_length=30)
    BirthDate = models.CharField(max_length=30, null=True, blank=True)
    Gender = models.CharField(max_length=20, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    PostalCode = models.CharField(max_length=10, null=True, blank=True)
    Country = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=30, null=True, blank=True)
    City = models.CharField(max_length=20, null=True, blank=True)
    TimeZone = models.CharField(max_length=30, null=True, blank=True)
    RegisteredDate = models.DateTimeField(null=True, blank=True)
    UpdatedDate = models.DateTimeField(null=True, blank=True)
    VerifiedCustomer = models.CharField(max_length=20, null=True)

    def str(self):
        return self.CustomerName


class Bank(models.Model):
    CustomerName = models.CharField(max_length=50, null=True, blank=True)
    BankName = models.CharField(max_length=50, null=True, blank=True)
    AccountNumber = models.FloatField(max_length=30, primary_key=True)
    AccountHolderName = models.CharField(max_length=30, null=True, blank=True)
    IFSCCode = models.CharField(max_length=11, null=True, blank=True)
    AccountType = models.CharField(max_length=15, null=True, blank=True)
    BankType = models.CharField(max_length=15, null=True, blank=True)
    DateCreated = models.DateTimeField(null=True, blank=True)
    DateModified = models.DateTimeField(max_length=30, null=True, blank=True)

    def str(self):
        return self.BankName


class Transaction(models.Model):
    # CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    LoyaltyTransactionId = models.CharField(max_length=30)
    CustomerId = models.CharField(max_length=30)  # changed float to char
    LoyaltyType = models.CharField(max_length=30, null=True, blank=True)
    TransactionType = models.CharField(max_length=20, null=True, blank=True)
    LoyaltyPoints = models.IntegerField()
    TransactionStatus = models.CharField(max_length=10, null=True, blank=True)
    TransactionDetails = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=30, null=True, blank=True)
    City = models.CharField(max_length=20, null=True, blank=True)
    TransactionTime = models.DateTimeField(primary_key=True)

    def str(self):
        return self.LoyaltyTransactionId


class Summary(models.Model):
    Redemption_Transaction_ID = models.AutoField(primary_key=True)
    Customer_Member_ID = models.FloatField()
    PartnerName = models.CharField(max_length=50, null=True, blank=True)
    CompanyName = models.CharField(max_length=50, null=True, blank=True)
    PAN_Card_Number = models.CharField(max_length=10, null=True, blank=True)
    GSTNumber = models.CharField(max_length=15, null=True, blank=True)
    City = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=30, null=True, blank=True)
    VoucherQuantity = models.IntegerField(null=True, blank=True)
    LoyaltyPoints = models.FloatField()
    ConversionRate = models.FloatField(null=True, blank=True)
    RedemptionValue = models.FloatField(null=True, blank=True)
    BankName = models.CharField(max_length=30, null=True, blank=True)
    BankAccountNumber = models.FloatField(max_length=18)
    BankAccountType = models.CharField(max_length=20, null=True, blank=True)
    BankIFSCCode = models.CharField(max_length=11, null=True, blank=True)
    RedemptionTarget = models.FloatField(null=True, blank=True)
