'''import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
eg = "A cat was chasing a mouse"
eg= [stemmer.stem(token) for token in eg.split(" ")]
print(" ".join(eg))

eg = "A cat was chasing a mouse. There was cacti around the corner"
lemmatizer = WordNetLemmatizer()
eg= [lemmatizer.lemmatize(token) for token in eg.split(" ")]
print(" ".join(eg))

print(lemmatizer.lemmatize('better',pos = 'a'))'''

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

