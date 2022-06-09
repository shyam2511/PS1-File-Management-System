

import mysql.connector


def conversiontosql(df):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="project")

    cursor = mydb.cursor()

    # Create Table

    # Insert DataFrame to Table
    for row in df.itertuples():
        cursor.execute('''
                    INSERT INTO products (product_id, product_name, price)
                    VALUES (%s,%s,%s)
                    ''',
                       (row.product_id,
                        row.product_name,
                        row[4]
                        ))
    mydb.commit()
    return 'updation successful'



