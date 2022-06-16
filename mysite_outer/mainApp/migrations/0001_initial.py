# Generated by Django 4.0.5 on 2022-06-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('CustomerName', models.CharField(blank=True, max_length=50, null=True)),
                ('BankName', models.CharField(blank=True, max_length=50, null=True)),
                ('AccountNumber', models.FloatField(max_length=30, primary_key=True, serialize=False)),
                ('AccountHolderName', models.CharField(blank=True, max_length=30, null=True)),
                ('IFSCCode', models.CharField(blank=True, max_length=11, null=True)),
                ('AccountType', models.CharField(blank=True, max_length=15, null=True)),
                ('BankType', models.CharField(blank=True, max_length=15, null=True)),
                ('DateCreated', models.DateTimeField(blank=True, null=True)),
                ('DateModified', models.DateTimeField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('EnterpriseName', models.CharField(blank=True, max_length=50, null=True)),
                ('CustomerName', models.CharField(max_length=50)),
                ('EmailId', models.EmailField(blank=True, max_length=30, null=True)),
                ('MobileNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('Status', models.CharField(blank=True, max_length=20, null=True)),
                ('ProfileComplete', models.CharField(blank=True, max_length=5, null=True)),
                ('KYCStatus', models.CharField(blank=True, max_length=20, null=True)),
                ('CustomerGroup', models.CharField(blank=True, max_length=30, null=True)),
                ('CurrentLoyaltyPoints', models.FloatField()),
                ('TotalLoyaltyPoints', models.FloatField()),
                ('LastRedemption', models.FloatField()),
                ('TotalRedemption', models.FloatField()),
                ('BonusUponTotal', models.CharField(max_length=30)),
                ('BirthDate', models.CharField(blank=True, max_length=30, null=True)),
                ('Gender', models.CharField(blank=True, max_length=20, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('PostalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('Country', models.CharField(blank=True, max_length=20, null=True)),
                ('State', models.CharField(blank=True, max_length=30, null=True)),
                ('City', models.CharField(blank=True, max_length=20, null=True)),
                ('TimeZone', models.CharField(blank=True, max_length=30, null=True)),
                ('RegisteredDate', models.DateTimeField(blank=True, null=True)),
                ('UpdatedDate', models.DateTimeField(blank=True, null=True)),
                ('VerifiedCustomer', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('Redemption_Transaction_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Customer_Member_ID', models.FloatField()),
                ('PartnerName', models.CharField(blank=True, max_length=50, null=True)),
                ('CompanyName', models.CharField(blank=True, max_length=50, null=True)),
                ('PAN_Card_Number', models.CharField(blank=True, max_length=10, null=True)),
                ('GSTNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('City', models.CharField(blank=True, max_length=20, null=True)),
                ('State', models.CharField(blank=True, max_length=30, null=True)),
                ('VoucherQuantity', models.IntegerField(blank=True, null=True)),
                ('LoyaltyPoints', models.FloatField()),
                ('ConversionRate', models.FloatField(blank=True, null=True)),
                ('RedemptionValue', models.FloatField(blank=True, null=True)),
                ('BankName', models.CharField(blank=True, max_length=30, null=True)),
                ('BankAccountNumber', models.FloatField(max_length=18)),
                ('BankAccountType', models.CharField(blank=True, max_length=20, null=True)),
                ('BankIFSCCode', models.CharField(blank=True, max_length=11, null=True)),
                ('RedemptionTarget', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('LoyaltyTransactionId', models.CharField(max_length=30)),
                ('CustomerId', models.CharField(max_length=30)),
                ('LoyaltyType', models.CharField(blank=True, max_length=30, null=True)),
                ('TransactionType', models.CharField(blank=True, max_length=20, null=True)),
                ('LoyaltyPoints', models.IntegerField()),
                ('TransactionStatus', models.CharField(blank=True, max_length=10, null=True)),
                ('TransactionDetails', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=20, null=True)),
                ('State', models.CharField(blank=True, max_length=30, null=True)),
                ('City', models.CharField(blank=True, max_length=20, null=True)),
                ('TransactionTime', models.DateTimeField(primary_key=True, serialize=False)),
            ],
        ),
    ]