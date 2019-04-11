import nltk
from nltk.stem import PorterStemmer,LancasterStemmer
st=PorterStemmer()
st1=LancasterStemmer()
print("\t\tPorter\t\tLancaster")

print('Singing - ',st.stem("Singing"),"\t",st1.stem("Singing"))
print('Generally - ',st.stem("Generally"),"\t",st1.stem("Generally"))
print('Happiness - ',st.stem("Happiness"),"\t",st1.stem("Happiness"))
print('Timely - ',st.stem("Timely"),"\t",st1.stem("Timely"))
print('Extraction - ',st.stem("Extraction"),"\t",st1.stem("Extraction"))
print('Mapping - ',st.stem("Mapping"),"\t",st1.stem("Mapping"))
print('Using - ',st.stem("Using"),"\t",st1.stem("Using"))
print('Apples - ',st.stem("Apples"),"\t",st1.stem("Apples"))
print('Blue - ',st.stem("Blue"),"\t",st1.stem("Blue"))
print('These - ',st.stem("These"),"\t",st1.stem("These"))