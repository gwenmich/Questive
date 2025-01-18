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
                "wears_glasses": bool(suspect_info[5]),
                "shirt_colour": suspect_info[6],
                "trouser_colour": suspect_info[7],
                "shoe_colour": suspect_info[8],
                "earring": bool(suspect_info[9]),
                "wears_a_hat": bool(suspect_info[10])
            })
        return suspect_details

    # Converts high score data into a dictionary
    @staticmethod
    def _high_score_dictionary(high_scores):
        top_ten_scores = []
        for score in high_scores:
            top_ten_scores.append({
                "id": int(score[0]),
                "score": int(score[1])
            })
        return top_ten_scores

    # checks if there is a valid database connection
    def check_database_connection(self, sql_query, dictionary):
        database_connection = None
        try:
            database_connection = self._connect_to_db()
            cur = database_connection.cursor()
            print("Connected to DB: %s" % DATABASE)

            query = sql_query
            cur.execute(query)

            result = cur.fetchall()
            results_dict = dictionary(result)
            print(results_dict)

            cur.close()
            return results_dict

        except Exception:
            raise DbConnectionError("Failed to read data from DB: %s" % DATABASE)

        finally:
            if database_connection:
                database_connection.close()
                print("%s connection is closed" % DATABASE)

    # Gets all suspects and their details from the database
    def get_suspects(self):
        all_suspects = """SELECT * FROM suspects ORDER BY name ASC;"""
        suspects_dict = self.check_database_connection(all_suspects, self._suspect_dictionary)
        return suspects_dict

    # Gets a random suspect and all their details from the database
    def get_random_suspect(self):
        random_suspect = """SELECT * FROM suspects ORDER BY RAND() LIMIT 1;"""
        random_suspect_dict = self.check_database_connection(random_suspect, self._suspect_dictionary)
        return random_suspect_dict

    # Gets high scores from the database
    def get_high_scores(self):
        high_scores = """SELECT * FROM high_scores ORDER BY score DESC;"""
        high_scores_dict = self.check_database_connection(high_scores, self._high_score_dictionary)
        return high_scores_dict


# IN DEVELOPMENT
# # Adds a new high score to the database
# def add_new_high_score(self, new_score):
#     new_high_score = """INSERT INTO high scores (score) VALUES (new_score);"""
#     print(f"NEW High Score added to db: {new_score}")
#     return self.get_high_scores()


# sample calls to test db_utils
if __name__ == "__main__":
    pass
# db_connection = DbConnection()
# db_connection.get_suspects()
# db_connection.get_random_suspect()
# db_connection.get_high_scores()
# db_connection.add_new_high_score(9)
