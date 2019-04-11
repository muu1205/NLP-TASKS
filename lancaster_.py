import nltk
from nltk.stem import LancasterStemmer
st1=LancasterStemmer()
print('Singing - ',st1.stem("Singing"))
print('Generally - ',st1.stem("Generally"))
print('Happiness - ',st1.stem("Happiness"))
print('Timely - ',st1.stem("Timely"))