#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:43:22 2023

@author: ayasewelam
"""

import PyPDF2
import os
import re
import math
os.chdir('/Users/ayasewelam/Desktop/MScFintech/dissertation/DICode/JPM')

# Bag of words for bottom technical level
bottom_technical_words = ['artificial intelligence', 'business intelligence', 'image understanding', 'investment decision support system',
                          'intelligent data analysis', 'intelligent robot', 'machine learning', 'deep learning', 'semantic search',
                          'biometric technology', 'face recognition', 'speech recognition', 'authentication', 'auto pilot', 'autopilot',
                          'natural language processing']

# Bag of words for big data technology
big_data_words = ['big data', 'data mining', 'text mining', 'data visualization', 'heterogeneous data',
                  'credit investigation', 'augmented reality', 'mixed reality', 'virtual reality']

# Bag of words for cloud computing technology
cloud_computing_words = ['cloud computing', 'flow calculation', 'figure calculation', 'memory calculation',
                         'secure multi-party computation', 'brain like computing', 'green computing',
                         'cognitive computing', 'fusion architecture', 'billion-level concurrency', 'eb level storage',
                         'internet of things', 'information physical system']

# Bag of words for blockchain technology
blockchain_words = ['blockchain', 'digital currency', 'distributed computing', 'differential privacy technology',
                    'smart financial contracts']

# Bag of words for practical application level
practical_application_words = ['mobile internet', 'industrial internet', 'mobile internet', 'internet medicine', 'electric commerce',
                               'mobile payment', 'third party payment', 'nfc payment', 'smart energy', 'b2b', 'c2b', 'c2c', '020',
                               'internet connection', 'smart wear', 'smart agriculture', 'intelligent transportation', 'intelligent medicine',
                               'intelligent customer', 'smart home', 'intelligent investment adviser', 'intelligent cultural tourism',
                               'intelligent environmental protection', 'smart grid', 'intelligent marketing', 'digital marketing',
                               'unmanned retail', 'online finance', 'digital finance', 'fintech', 'financial technology',
                               'quantitative finance', 'open bank']

def count_matching_words(text, bag_of_words):
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Count the occurrences of matching words in the text
    matching_words_count = sum([text.count(word) for word in bag_of_words])

    return matching_words_count

# Example usage
file_path = 'JPM2019.pdf'

# Extract text from the PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

text = extract_text_from_pdf(file_path)

# Count the occurrences of words for each category
bottom_technical_count = count_matching_words(text, bottom_technical_words)
big_data_count = count_matching_words(text, big_data_words)
cloud_computing_count = count_matching_words(text, cloud_computing_words)
blockchain_count = count_matching_words(text, blockchain_words)
practical_application_count = count_matching_words(text, practical_application_words)

# Calculate the digital adoption index using logarithmic processing
digital_adoption_index = (
    math.log(bottom_technical_count + 1) +
    math.log(big_data_count + 1) +
    math.log(cloud_computing_count + 1) +
    math.log(blockchain_count + 1) +
    math.log(practical_application_count + 1)
)

print("Digital Adoption Index:", digital_adoption_index)
print("Occurrences in Bottom Technical Level:", bottom_technical_count)
print("Occurrences in Big Data Technology:", big_data_count)
print("Occurrences in Cloud Computing Technology:", cloud_computing_count)
print("Occurrences in Blockchain Technology:", blockchain_count)
print("Occurrences in Practical Application Level:", practical_application_count)

