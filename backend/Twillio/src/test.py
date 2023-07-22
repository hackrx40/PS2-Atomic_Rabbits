import mysql.connector


def msql_connection(a:str):
    database = 'hackrx'
    user = 'root'
    password = '2424arKA@@'
    host = 'localhost'
    cursor=None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306
        )
        if connection.is_connected():
            print("Connected to MySQL database!")

            # Perform database operation - execute a simple query
            cursor = connection.cursor()

            # Execute a simple query
            cursor.execute(a)

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            return rows

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if(cursor is not None):
            cursor.close()
            connection.close()
            
def msql_connection2(a:str):
    database = 'hackrx'
    user = 'root'
    password = '2424arKA@@'
    host = 'localhost'
    cursor=None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306
        )
        if connection.is_connected():
            print("Connected to MySQL database!")

            # Perform database operation - execute a simple query
            cursor = connection.cursor()

            # Execute a simple query
            cursor.execute(a)

            # Fetch all rows from the result set

            return "Done"

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if(cursor is not None):
            cursor.close()
            connection.close()
