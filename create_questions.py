import json
import spacy
import sqlite3

nlp = spacy.load('en_core_web_sm')

print(nlp)
print('success')

def get_all():
    try:
        sqliteConnection = sqlite3.connect('/data/lingomooAPP.db')
        sqliteConnection.row_factory = sqlite3.Row  
        cursor = sqliteConnection.cursor()

        print("Connected to SQLite")

        sql_select_query = """SELECT * FROM sentences"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        for row in records:
            print(dict(row))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The SQLite connection is closed")

get_all()
