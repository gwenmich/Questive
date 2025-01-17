# for getting information from the database

import mysql.connector
from db_config import HOST, USER, PASSWORD, DATABASE


# Raised if a connection exception occurs in the script below
class DbConnectionError(Exception):
    pass


# Database connection
def _connect_to_db():
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=DATABASE
    )
    return connection


# Converts suspect(s) query into a dictionary
def _suspect_dictionary(suspect):
    suspect_details = []
    for suspect_info in suspect:
        suspect_details.append({
            "id": int(suspect_info[0]),
            "name": suspect_info[1],
            "age": int(suspect_info[2]),
            "hair_colour": suspect_info[3],
            "eye_colour": suspect_info[4],
            "height": int(suspect_info[5]),
            "piercing": bool(suspect_info[6]),
            "tattoo": bool(suspect_info[7]),
            "wears_a_hat": bool(suspect_info[8]),
            "occupation": suspect_info[9],
            "country": suspect_info[10]
        })
    return suspect_details


# Gets the complete list of pizzas along with their toppings from the database
def get_random_suspect():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM suspects ORDER BY RAND() LIMIT 1;"""

        cur.execute(query)
        suspect = cur.fetchall()
        print(suspect)
        suspect_info = _suspect_dictionary(suspect)
        print(suspect_info)
        cur.close()

        return suspect

    except Exception:
        raise DbConnectionError("Failed to read data from DB: %s" % DATABASE)

    finally:
        if db_connection:
            db_connection.close()
            print("%s connection is closed" % DATABASE)


# sample calls to test db_utils
if __name__ == "__main__":
    get_random_suspect()