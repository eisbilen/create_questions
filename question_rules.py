rules = {
            'PREPOSITION':[[{'TAG': 'IN'}]],

            'ADVERB':[[{'POS': 'ADV'}]],
            'ADJECTIVE':[[{'POS': 'ADJ'}]],
            
            'VERB1':[[{'TAG': 'VBN'}]],
            'VERB2':[[{'TAG': 'VB'}]],
            'VERB3':[[{'TAG': 'VBZ'}]],
            'VERB4':[[{'TAG': 'VBP'}]],
            
            'VERB':[[{'POS': 'VERB'}]],
            'AUX':[[{'POS': 'AUX'}]],

            'NOUN':[[{'POS': 'NOUN'}]],
            'NOUN_P':[[{'TAG': 'NNS'}]],

            'DETERMINER':[[{'POS': 'DET'}]],
            'WH-DETERMINER':[[{'TAG': 'WDT'}]],
            'PRE-DETERMINER':[[{'TAG': 'PDT'}]],

            'CONJUCTION':[[{'TAG': 'CC'}]],
            'ADVERB-PARTICLE':[[{'TAG': 'RP'}]],

            'COMPARATIVE-ADJECTIVE':[[{'TAG': 'JJR'}]],
            'SUPERLATIVE-ADJECTIVE':[[{'TAG': 'JJS'}]],

            'COMPARATIVE-ADVERB':[[{'TAG': 'RBR'}]],
            'SUPERLATIVE-ADVERB':[[{'TAG': 'RBS'}]],

            'THERE-IS':[[{'TEXT': 'There', 'TEXT': 'there'}, {'TEXT': 'is', 'TEXT': 'are'}]],
            'MODAL':[[{'TAG': 'MD'}]],           
        }




#to_infinitive_rule_1 = [{'TAG': 'TO'}, {'TAG': 'VB'}]
#gerunds_rule_1 = [{'TAG': 'VB'}, {'TAG': 'VBG'}]

#passive_rule_1 = [{'DEP': 'auxpass'}, {'TAG': 'VBN'}]
#subject_rule_1 = [{'DEP': 'csubj'}]
#subject_rule_2 = [{'DEP': 'nsubj'}]
#object_rule_1 = [{'DEP': 'dobj'}]

# Future Tenses With Auxiliaries
#future_tense_rule_1 = [{'TEXT': 'will'}, {'TAG': 'VB'}]
#future_tense_rule_2 = [{'TEXT': 'shall'}, {'TAG': 'VB'}]

# Morphological Present Tenses
#simple_present_rule_1 = [{'POS': 'PRON'}, {'TAG': 'VBP', 'TAG': 'VBZ'}, {
#    'TAG': 'VB', 'TAG': 'VBG', 'TAG': 'VBN', 'OP': '!'}]
#present_continuous_rule_1 = [
#    {'TAG': 'VBZ', 'DEP': 'aux'}, {'TAG': 'VBG', 'DEP': 'ROOT'}]
#present_perfect_rule_1 = [
#    {'TAG': 'VBZ', 'DEP': 'aux'}, {'TAG': 'VBN', 'DEP': 'ROOT'}]
#present_perfect_continuous_rule_1 = [{'TAG': 'VBZ', 'DEP': 'aux'}, {
#    'TAG': 'VBN'}, {'TAG': 'VBN', 'DEP': 'ROOT'}]

# Morphological Past Tenses
#simple_past_rule_1 = [{'POS': 'PRON'}, {'TAG': 'VBD'}, {
#    'TAG': 'VB', 'TAG': 'VBG', 'TAG': 'VBN', 'OP': '!'}]

# Possessive Endings the boy's ball
#possesive_ending_rule_1 = [{'TAG': 'POS'}]

# Possessive Pronoun
#possesive_pronoun_rule_1 = [{'TAG': 'PRP$'}]