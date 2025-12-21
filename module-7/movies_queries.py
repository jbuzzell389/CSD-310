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

cursor = db.cursor(buffered=True)

cursor.execute("SELECT studio_id, studio_name FROM studio")
movies = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --\n")
for studio in movies:
    print(f"Studio ID:{studio[0]}")
    print(f"Studio Name:{studio[1]}\n")

cursor.execute("SELECT genre_id, genre_name FROM genre")
movies = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --\n")
for genre in movies:
    print(f"Genre ID:{genre[0]}")
    print(f"Genre Name:{genre[1]}\n")

#
cursor.execute("""
    SELECT film_name, film_runtime
    FROM film
    WHERE film_runtime < 120
""")

movies = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --\n")
for film in movies:
    print(f"Film Name:{film[0]}")
    print(f"Runtime:{film[1]}\n")


cursor.execute("""
    SELECT film_name, film_director
    FROM film
    ORDER BY film_director
""")

movies = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --\n")
for film in movies:
    print(f"Film Name:{film[0]}")
    print(f"Director:{film[1]}\n")



          

          
