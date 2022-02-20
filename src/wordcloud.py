

# Here are all the installs and imports you will need for your word cloud script and uploader widget


import wordcloud
import numpy as np
from matplotlib import pyplot as plt

#Insert the content
file_contents=""

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    #Make all the characters alphabets and ignore case
    file_contents.isalpha()
    individual_words=file_contents.lower().split()
    new_words={}
    for word in sep:
        if word not in uninteresting_words and word not in punctuations:
            
            if word not in new_words:
                new_words[word]=1
            else:
                new_words[word]+=1
            
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(new_words)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
