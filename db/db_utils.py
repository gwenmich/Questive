import mysql.connector
from db.db_config import HOST, USER, PASSWORD, DATABASE


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
                "suspect_id": int(suspect_info[0]),
                "name": suspect_info[1],
                "hair_colour": suspect_info[2],
                "eye_colour": suspect_info[3],
                "wears_glasses": "wears glasses" if bool(suspect_info[4]) == True else "doesn't wear glasses",
                "shirt_colour": suspect_info[5],
                "trouser_colour": suspect_info[6],
                "shoe_colour": suspect_info[7],
                "wears_a_hat": "wears a hat" if bool(suspect_info[8]) == True else "doesn't wear a hat"
            })
        return suspect_details

    # Converts high score data into a dictionary
    @staticmethod
    def _high_score_dictionary(high_scores):
        top_ten_scores = []
        for score in high_scores:
            top_ten_scores.append({
                "player_id": int(score[0]),
                "score": int(score[1])
            })
        return top_ten_scores

    # checks if there is a valid database connection
    def check_database_connection(self, sql_query, dictionary):
        database_connection = None
        try:
            database_connection = self._connect_to_db()
            cur = database_connection.cursor()
            # print("Connected to DB: %s" % DATABASE) helpful for debugging

            query = sql_query
            cur.execute(query)

            result = cur.fetchall()
            results_dict = dictionary(result)
            # print(results_dict) helpful for testing/debugging

            cur.close()
            return results_dict

        except Exception:
            raise DbConnectionError("Failed to read data from DB: %s" % DATABASE,
                                    " Check you've entered username and password in db/db_config.")
        finally:
            if database_connection:
                database_connection.close()
                # print("%s connection is closed" % DATABASE) helpful for debugging

    # Gets all suspects and their details from the database
    def get_suspects(self):
        all_suspects = """SELECT * FROM suspects ORDER BY name ASC;"""
        suspects_dict = self.check_database_connection(all_suspects, self._suspect_dictionary)
        return suspects_dict

    # Gets a random suspect and all their details from the database
    def get_murderer(self):
        murderer = """SELECT * FROM suspects ORDER BY RAND() LIMIT 1;"""
        murderer_dict = self.check_database_connection(murderer, self._suspect_dictionary)
        print(f"The murderer is {murderer_dict[0]["name"]}") # keep in for testing, uncomment for actual game play
        return murderer_dict

    # Gets high scores from the database
    def get_high_scores(self):
        high_scores = """SELECT * FROM high_scores ORDER BY score DESC;"""
        high_scores_dict = self.check_database_connection(high_scores, self._high_score_dictionary)
        return high_scores_dict

    # Replaces lowest score with new high score in db
    def update_high_scores(self, new_high_score):
        database_connection = None
        try:
            database_connection = self._connect_to_db()
            cur = database_connection.cursor()
            # print("Connected to DB: %s" % DATABASE) helpful for debugging

            # The middle SELECT/FROM is required due to an mySQL limitation, which won't allow direct access to the
            # end subquery due to a modifying/reading table conflict in immediate queries
            query = """
            UPDATE high_scores 
            SET score = %s 
            WHERE player_id = (
                SELECT player_id 
                FROM (
                    SELECT player_id 
                    FROM high_scores 
                    ORDER BY score ASC 
                    LIMIT 1
                    ) AS SUBQUERY
            );"""
            # The above subquery selects the player with the lowest score

            cur.execute(query, [new_high_score])
            database_connection.commit()  # Commits permanent save to db required for INSERTS/UPDATES

            cur.close()

            return self.get_high_scores()

        except Exception:
            raise DbConnectionError("Failed to read data from DB: %s" % DATABASE)
        finally:
            if database_connection:
                database_connection.close()
                # print("%s connection is closed" % DATABASE) helpful for debugging


# sample calls to test db_utils
if __name__ == "__main__":
    pass
    # db_connection = DbConnection()
    # db_connection.get_suspects()
    # db_connection.get_random_suspect()
    # db_connection.get_high_scores()
    # db_connection.update_high_scores(12)
