# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:00:58 2020

@author: Acer
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
# from num2words import num2words

import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math

import csv
import re
from datetime import datetime

import openpyxl

def makes_csv(com, sim_content,sin_comment , word ,freq,no_of_sentences,length_of_comment,num_of_punctuations,stop_word_ratio,post_coment_gap,is_black_word,link_mail_pnumber,comment_duplication):
        
        list_values = [com, sim_content,sin_comment, word,freq,no_of_sentences,length_of_comment,num_of_punctuations,stop_word_ratio,post_coment_gap,is_black_word,link_mail_pnumber,comment_duplication]
        
        stringList = [str(x) for x in list_values]  # convert all fields values to string value
        return stringList
        
    
def create_file(fields_list):
    
    
    fields =  ['comment_id', 'similerity_content','similerity_commemt','wordCount','wordRedundantRatio','noOfSentences','lengthOfComment','numberOfPunctuations','stopWordRatio','post_coment_gap','is_black_word','linkMailLinkAvailable','comment_duplication']
    rows = fields_list
    
    filename = "data.csv"
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(fields)  
        writer.writerows(rows)    