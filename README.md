This code was developed as part of my dissertation to analyze the usage of digital technology-related words in the financial industry from the year 2008, marked by the economic crisis, to 2022. The primary focus was on understanding the impact of digital technology on financial industry-related risks, especially bankruptcy risk. As there was no proxy available to compute digital transformation within the banking industry, this code was specifically created to process standardized 10-K files commonly used in the financial sector.

Overview
The code utilizes Python to analyze PDF files of financial reports (10-K filings) and compute the frequency of digital finance-related words. It categorizes words into different technological levels, including technical, big data, cloud computing, blockchain, and practical application levels.

Usage
Set File Directory: Update the code to specify the directory containing your PDF files.
os.chdir('set file directory')

Define Bag of Words: Add the required words for each technological level in their respective lists.
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

Run the Code: Execute the Python script on a PDF file to obtain the digital adoption index and word occurrences in each category.
# Example usage - set pdf file required as 
file_path = 'xxx.pdf'

Results
The script calculates the Digital Adoption Index using logarithmic processing based on the occurrences of words in each category. 
The results include the overall Digital Adoption Index and the occurrences at different technological levels.
print("Digital Adoption Index:", digital_adoption_index)
print("Occurrences in Bottom Technical Level:", technical_count)
print("Occurrences in Big Data Technology:", big_data_count)
print("Occurrences in Cloud Computing Technology:", cloud_computing_count)
print("Occurrences in Blockchain Technology:", blockchain_count)
print("Occurrences in Practical Application Level:", practical_application_count)
