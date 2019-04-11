import nltk
from nltk.stem import RegexpStemmer
st1=RegexpStemmer('ing')
print("Learning - ",st1.stem('Learning'))
print("Singing - ",st1.stem('Singing'))

print()

st2=RegexpStemmer('na')
print("Banana - ",st2.stem('Banana'))