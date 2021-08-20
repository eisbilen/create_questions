import json
import spacy
from spacy.matcher import Matcher

from add_options import AddOptions
import question_rules as qr
import tag_list as tag_list

import sqlite3

nlp = spacy.load('en_core_web_md')
taglist = tag_list.taglist

class QuestionFilter:
    def __init__(self, taglist, my_doc) -> None:
        self.taglist = taglist
        self.my_doc = my_doc
        self.__rule = list()
        self.__matcher = list()

        for i in range(len(taglist)):
            self.__rule.append(qr.rules[taglist[i]])
            self.__matcher.append(Matcher(nlp.vocab))
            self.__matcher[i].add(taglist[i], self.__rule[i])

    def __call__(self):
        return self.write_linguistic_features()
        
    def write_linguistic_features(self):
        lf_dict = {}
        comp_lf_dict = {}

        
        for i in range(len(taglist)):
            matches = self.__matcher[i](self.my_doc)
            question_list = []
            option_list = []
            for match_id, start, end in matches:
                
                lf_dict = {}
                # Get the string representation
                string_id = nlp.vocab.strings[match_id]
                span = self.my_doc[start:end]  # The matched span
                lf_dict[string_id] = span.text
 
                if lf_dict:
                    question_list.append(lf_dict)
                    temp = AddOptions(self.taglist[i], lf_dict)
                    option_list.append(temp.add_options())
                    print('option list')
                
            question_list.insert(0, option_list)
            comp_lf_dict[self.taglist[i]] = question_list

        return comp_lf_dict
    
    def include_options(self, item, vocab):
        temp = AddOptions(self.tag, self)

        if vocab==0:
            item.insert(0,item.add_options())
        else:
            item.insert(0, item.add_options_vocab(nlp, vocab))
        return 

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
            print(QuestionFilter(taglist, my_doc)())
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

get_all()
