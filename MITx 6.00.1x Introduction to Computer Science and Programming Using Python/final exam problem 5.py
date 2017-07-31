# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:15:59 2017

@author: Polla
Final Exam   Problem 5

map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping.
"""
#Notes
#return a tuple (key_code, decoded)
#key_code = {'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}

def create_dict(map_from, map_to, code):
#    print (map_from)
#    print(map_to)
#    print(code)
    i=0
    dict_cipher=dict()
    for i in range(len(map_from)):
        key=map_from[i]
        value=map_to[i]
        try:
            dict_cipher[key]=value
        except:
            pass
    return dict_cipher

def coding(dict_cipher, code):
    l_message=list()
    for letter in code:
        l_message.append(dict_cipher[letter])
    s_message=''.join(l_message)
    return s_message


def cipher(map_from, map_to, code):
    #create a cipher dictionary
    dict_cipher=dict()
    dict_cipher=create_dict(map_from, map_to, code)
#    print(dict_cipher)

    #code the message
    message=coding(dict_cipher, code)
#    print(message)

    #compile the result as the requested format
    result=(dict_cipher, message)
#    print(result)
    return result
    
#Test Case 1
#({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
cipher("abcd", "dcba", "dab")


