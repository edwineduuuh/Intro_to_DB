# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database)
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="@Lonewolf92" 
    )

    if conn.is_connected():
        cursor = conn.cursor()
        # Create the database; IF NOT EXISTS ensures no error if it already exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection safely
    if 'cursor' in locals():
        cursor.close()

    if 'conn' in locals() and conn.is_connected():
        conn.close()
