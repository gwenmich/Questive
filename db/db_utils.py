# for getting information from the database

import mysql.connector
from db_config import HOST, USER, PASSWORD, DATABASE


# Raised if a connection exception occurs in the script below
class DbConnectionError(Exception):
    pass


class DbConnection:
    # Database connection
    @staticmethod
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
    @staticmethod
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

    # checks if there is a valid database connection
    def check_database_connection(self, sql_query):
        db_connection = None
        try:
            db_connection = self._connect_to_db()
            cur = db_connection.cursor()
            print("Connected to DB: %s" % DATABASE)

            query = sql_query

            cur.execute(query)
            result = cur.fetchall()
            results_dict = self._suspect_dictionary(result)
            print(results_dict)

            cur.close()
            return results_dict

        except Exception:
            raise DbConnectionError("Failed to read data from DB: %s" % DATABASE)

        finally:
            if db_connection:
                db_connection.close()
                print("%s connection is closed" % DATABASE)

    # Gets all suspects and their details from the database
    def get_suspects(self):
        all_suspects = """SELECT * FROM suspects ORDER BY name ASC;"""
        suspects_dict = self.check_database_connection(all_suspects)
        return suspects_dict

    # Gets a random suspect and all their details from the database
    def get_random_suspect(self):
        random_suspect = """SELECT * FROM suspects ORDER BY RAND() LIMIT 1;"""
        random_suspect_dict = self.check_database_connection(random_suspect)
        return random_suspect_dict


# sample calls to test db_utils
if __name__ == "__main__":
    pass
    # db_connection = DbConnection()
    # db_connection.get_suspects()
    # db_connection.get_random_suspect()
