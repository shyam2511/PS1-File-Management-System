from django.http import HttpResponse
from django.shortcuts import render
from .convert import conversiontosql
from .convertback import converttocsv
import pandas as pd
import mimetypes
import os

def index(request):
    return render(request, 'login.html')


def dashboard(request):
    username = request.GET['username']

    return render(request, 'dashboard.html', {'name': username})


def upload(request):
    if request.method == 'POST':
        data = request.FILES['myfile']
        df = pd.read_csv(data)
        cdres = conversiontosql(df)
    return render(request, 'output.html', {'result': cdres})


# Define function to download pdf file using template
def download(request):
    converttocsv()
    filename='output.csv'
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
