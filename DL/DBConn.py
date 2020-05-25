from termcolor import colored
import mysql.connector


def return_connection():
    try:
        connection = mysql.connector.connect(option_files='data.conf')
        print("Connecting to database - " + colored("Success", "green"))
        return connection
    except Exception as e:
        print("Connecting to database - " + colored("Failure", "red"))
        return None
