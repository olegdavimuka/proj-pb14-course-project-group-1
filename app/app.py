import os
import requests
import aiogram
import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect(
        database="bot_data", user="admin", host="db", password="password", port=5432
    )

    with conn.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS working_test(
                id serial PRIMARY KEY,
	            test_data VARCHAR ( 50 ) NOT NULL
            );
            """
        )
        cursor.execute(
            "INSERT INTO working_test(test_data) VALUES('DB connections is working')"
        )

        cursor.execute("SELECT test_data FROM working_test")

        for row in cursor.fetchall():
            print(row[0])
            assert row[0] == "DB connections is working"

    print("Bot is working")

