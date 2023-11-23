import psycopg2
from os import environ

if __name__ == "__main__":
    conn = psycopg2.connect(
        database=environ.get("PG_DB_NAME"), user=environ.get("PG_USER"), host="db", password=environ.get("PG_USER_PASSWORD"), port=5432
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
