import pandas as pd

import mysql.connector
import os
from django.conf import settings


def converttocsv():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="project")

    sql_query = pd.read_sql_query(''' 
                                  select * from mainapp_summary
                                  '''
                                  ,
                                  conn)  # here, the 'conn' is the variable that contains your database connection
    # information from step 2

    filepath = os.path.join(settings.BASE_DIR, 'converted_files\output.csv')
    if os.path.exists(filepath):
        os.remove(filepath)

    df = pd.DataFrame(sql_query)
    df.to_csv(r'.\converted_files\output.csv', index=True)
