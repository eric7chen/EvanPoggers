import pandas as pd
from ast import literal_eval

words_df = pd.read_csv("words.csv")
words_df.columns = ['Words', 'Values']

array = literal_eval(words_df.loc[words_df['Words'] == 'zoom']['Values'].to_string(index=False))

