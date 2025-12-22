""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values


#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

cursor = db.cursor()

def display_films(cursor, title):
    print(f"\n-- DISPLAYING {title} --\n")

    cursor.execute("""
        SELECT
        film.film_name AS Name,
            film.film_director AS 'Director',
            genre.genre_name AS 'Genre',
            studio.studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre
            ON film.genre_id = genre.genre_id
        INNER JOIN studio
            ON film.studio_id = studio.studio_id
    """)

    movies = cursor.fetchall()

    for film in movies:
        print(
            f"Film Name: {film[0]}\n"
            f"Director: {film[1]}\n"
            f"Genre: {film[2]}\n"
            f"Studio: {film[3]}\n"
    )

display_films(cursor, "FILMS")

cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime,
    film_director, studio_id, genre_id)
        VALUES ('Avatar', '2009', 162, 'James Cameron', 1, 2)
""")

display_films(cursor, "FILMS AFTER INSERT")

cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
""")

display_films(cursor, "FILMS AFTER UPDATE- Changed Alien to Horror")

cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Gladiator'
""")

display_films(cursor, "FILMS AFTER DELETE")