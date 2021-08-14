import json
import spacy
from spacy.matcher import Matcher

import question_rules as qr
import sqlite3

nlp = spacy.load('en_core_web_sm')

print(nlp)
print('success')

class QuestionFilter:
    def __init__(self, tag, my_doc) -> None:
        self.tag = tag
        self.my_doc = my_doc
        self.__rule = qr.rules[tag]
        self.__matcher = Matcher(nlp.vocab)
        self.__matcher.add(tag, self.__rule)
        self.__matches = self.__matcher(self.my_doc)
        
    def write_linguistic_features(self):
        lf_dict = {}
        lf_list = []
        for match_id, start, end in self.__matches:
            lf_dict = {}
            # Get the string representation
            string_id = nlp.vocab.strings[match_id]
            span = self.my_doc[start:end]  # The matched span
            lf_dict[string_id] = span.text
            lf_list.append(lf_dict)
            # print(match_id, string_id, start, end, span.text)
        return lf_list

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
            sentence = dict(row)['sentence']
            my_doc = nlp(sentence)
            print(my_doc)
            
            lf = QuestionFilter('PREPOSITIONS', my_doc).write_linguistic_features()
            lf1 = QuestionFilter('VERB1', my_doc).write_linguistic_features()
            lf2 = QuestionFilter('VERB2', my_doc).write_linguistic_features()
            lf3 = QuestionFilter('VERB3', my_doc).write_linguistic_features()

            print(lf)
            print(lf1)
            print(lf2)
            print(lf3)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

get_all()
