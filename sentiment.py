import pandas as pd
import string
import re
from ast import literal_eval
import nltk
import fuzzywuzzy as fuzz
from fuzzywuzzy import process

# Remove Punctuation

text = "i hate kaden"

text = "".join([char for char in text if char not in string.punctuation])
text = re.sub('[0-9]+', '', text)

# Tokenize

text = re.split('\W+', text)

# Remove Stopwords

stopwords = nltk.corpus.stopwords.words('english')

text = [word for word in text if word not in stopwords]

# Stemming and Lammitization

ps = nltk.PorterStemmer()

text = [ps.stem(word) for word in text]

wn = nltk.WordNetLemmatizer()

text = [wn.lemmatize(word) for word in text]

# Fuzzy search for best match
words_df = pd.read_csv("words.csv")

word = text[0]

process.extract(word, words_df, scorer = fuzz.ratio, limit = 1)

# Find value from words.csv

words_df.columns = ['Words', 'Values']

array = literal_eval(words_df.loc[words_df['Words'] == 'zoom']['Values'].to_string(index=False))

