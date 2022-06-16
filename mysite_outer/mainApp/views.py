from django.http import HttpResponse
from django.shortcuts import render
from .convertback import converttocsv
import pandas as pd
import mimetypes
import os
from email.errors import InvalidMultipartContentTransferEncodingDefect
from django.shortcuts import redirect
from django.http import HttpResponse, response
from tablib import Dataset
import pandas as pd
import datetime as datetime
from .models import Bank
from .models import Customer
from .models import Transaction
from django.db import connection

def index(request):
    return render(request, 'login.html')


def dashboard(request):


    return render(request, 'dashboard.html')

def upload(request):
    if request.method == 'POST':
        file1=request.FILES['myfile1']
        file2=request.FILES['myfile2']
        file3=request.FILES['myfile3']
        allFiles=[]
        allFiles.append(file1)
        allFiles.append(file2)
        allFiles.append(file3)
        print(allFiles)
        for file in allFiles:
            filename = file.name.split('.')[0].lower()
            print(filename)
            imported_data = pd.read_csv(file)
            data = imported_data.dropna(how="all")
            data.fillna('', inplace=True)
            data = data.values.tolist()
            if 'bank' in filename:
                for row in data:
                    row[7] = datetime.datetime.strptime(row[7], "%d-%m-%Y %H:%M")
                    row[8] = datetime.datetime.strptime(row[8], "%d-%m-%Y %H:%M")
                    value = Bank(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8]
                    )
                    value.save()

            elif 'customer' in filename:
                for row in data:
                    print(str(row[0])+'hello')
                    row[22] = datetime.datetime.strptime(row[22], "%d-%m-%Y %H:%M")
                    if len(row[14]) == 0:
                        row[14] = '2000-01-01'
                    row[23] = datetime.datetime.strptime(row[23], "%d-%m-%Y %H:%M")
                    row[0]=str(row[0])
                    print(type(row[0]))
                    print(len(row[0]))
                    value = Customer(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                        row[14],
                        row[15],
                        row[16],
                        row[17],
                        row[18],
                        row[19],
                        row[20],
                        row[21],
                        row[22],
                        row[23],
                        row[24]
                    )
                    value.save()

            elif 'transaction' in filename:
                for row in data:
                    row[10] = datetime.datetime.strptime(row[10], "%d-%m-%Y %H:%M")
                    print(type(row[10]))
                    value = Transaction(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10]
                    )
                    value.save()

    trans = Transaction.objects.all()
    cursor = connection.cursor()

    for t in trans:
        cursor.execute(
            "Update mainApp_customer set mainApp_customer.CurrentLoyaltyPoints = (%s), mainApp_customer.TotalLoyaltyPoints=mainApp_customer.TotalLoyaltyPoints+%s, mainApp_customer.UpdatedDate=%s where mainApp_customer.CustomerId = (%s) && mainApp_customer.UpdatedDate< (%s)",
            (t.LoyaltyPoints, t.LoyaltyPoints, t.TransactionTime, t.CustomerId, t.TransactionTime))

        cursor.execute("delete from mainApp_Summary;")
        cursor.execute(
            "Insert into mainApp_Summary(Customer_Member_ID, CompanyName, City, State, LoyaltyPoints, BankName, BankAccountNumber, BankAccountType, BankIFSCCode) "
            "SELECT mainApp_Customer.CustomerId, mainApp_Customer.EnterpriseName, mainApp_Customer.City, mainApp_Customer.State, mainApp_Customer.TotalLoyaltyPoints,mainApp_Bank.BankName, mainApp_Bank.AccountNumber, mainApp_Bank.AccountType, mainApp_Bank.IFSCCode FROM "
            "mainApp_Customer inner join mainApp_Bank on mainApp_Customer.CustomerName=mainApp_Bank.CustomerName")

    return render(request, 'output.html', {})

# Define function to download pdf file using template
def download(request):
    converttocsv()
    filename = 'output.csv'
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
    # Define the full file path
    filepath = BASE_DIR + '\\converted_files\\output.csv'
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
