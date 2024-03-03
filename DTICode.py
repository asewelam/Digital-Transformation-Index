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
os.chdir('set file directory')

# Bag of words for technical level
technical_words = ['insert required words']

# Bag of words for big data technology
big_data_words = ['insert required words; each as string in quotations']

# Bag of words for cloud computing technology
cloud_computing_words = ['insert required words; each as string in quotations']

# Bag of words for blockchain technology
blockchain_words = ['insert required words; each as string in quotations']

# Bag of words for practical application level
practical_application_words = ['insert required words; each as string in quotations']

def count_matching_words(text, bag_of_words):
    # Remove punctuation and convert text to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Count the occurrences of matching words in the text
    matching_words_count = sum([text.count(word) for word in bag_of_words])

    return matching_words_count

# Example usage - set pdf file required as 
file_path = 'xxx.pdf'

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
technical_count = count_matching_words(text, technical_words)
big_data_count = count_matching_words(text, big_data_words)
cloud_computing_count = count_matching_words(text, cloud_computing_words)
blockchain_count = count_matching_words(text, blockchain_words)
practical_application_count = count_matching_words(text, practical_application_words)

# Calculate the digital adoption index using logarithmic processing
digital_adoption_index = (
    math.log(technical_count + 1) +
    math.log(big_data_count + 1) +
    math.log(cloud_computing_count + 1) +
    math.log(blockchain_count + 1) +
    math.log(practical_application_count + 1)
)

print("Digital Adoption Index:", digital_adoption_index)
print("Occurrences in Bottom Technical Level:", technical_count)
print("Occurrences in Big Data Technology:", big_data_count)
print("Occurrences in Cloud Computing Technology:", cloud_computing_count)
print("Occurrences in Blockchain Technology:", blockchain_count)
print("Occurrences in Practical Application Level:", practical_application_count)

