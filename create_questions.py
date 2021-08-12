import json
import spacy
from spacy.matcher import Matcher

import sqlite3

nlp = spacy.load('en_core_web_sm')
matcher_prepositions_sub_conj = Matcher(nlp.vocab)
prepositions_sub_conj_rule_1 = [[{'TAG': 'IN'}]]
matcher_prepositions_sub_conj.add('PREPOSITION', prepositions_sub_conj_rule_1)

print(nlp)
print('success')

def write_linguistic_features(matches_single, my_doc):
    lf_dict = {}
    lf_list = []
    for match_id, start, end in matches_single:
        lf_dict = {}
        # Get the string representation
        string_id = nlp.vocab.strings[match_id]
        span = my_doc[start:end]  # The matched span
        lf_dict[string_id] = span.text
        lf_list.append(lf_dict)
        print(match_id, string_id, start, end, span.text)
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
            matches_prepositions_sub_conj = matcher_prepositions_sub_conj(my_doc)
            preposition = write_linguistic_features(matches_prepositions_sub_conj, my_doc)
            print(preposition)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The SQLite connection is closed")

get_all()
