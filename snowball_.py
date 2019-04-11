import nltk
from nltk.stem import SnowballStemmer
SnowballStemmer.languages
fr_st=SnowballStemmer('french')
print(ft_st.stem('manger'))