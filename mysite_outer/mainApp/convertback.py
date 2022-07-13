import pandas as pd

import mysql.connector


def converttocsv():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="project")

    sql_query = pd.read_sql_query(''' 
                                  select * from mainapp_summary
                                  '''
                                  ,
                                  conn)  # here, the 'conn' is the variable that contains your database connection
    # information from step 2

    # filepath = os.path.join(settings.BASE_DIR, 'converted_files\output.xlsx')
    # if os.path.exists(filepath):
    # os.remove(filepath)

    df = pd.DataFrame(sql_query)
    with pd.ExcelWriter(r'.\converted_files\output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Summary', na_rep='', float_format=None, columns=None,
                    header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True,
                    encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)
        for rows in df.itertuples():
            print(rows)
            sheet_name = str(rows[2])
            df1 = df.copy()
            df1 = df1.iloc[0:0]
            df1 = df1.append([rows])
            df1.to_excel(writer, sheet_name=sheet_name, na_rep='', float_format=None, columns=None,
                         header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None,
                         merge_cells=True,
                         encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)
    # df.to_csv(r'.\converted_files\output.csv', index=True)
