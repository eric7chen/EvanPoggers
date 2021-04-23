import os
import sys
import csv
import copy
import tweepy as tw
import pandas as pd

words_dictionary = {}
sentiment_list = []
word_file = open("words_sentiment.txt")

i = 1
for line in word_file:
    if i == 10:
        key = line.split()[0]
        sentiment_list.append(line.split()[2])
        words_dictionary[key] = copy.deepcopy(sentiment_list) # add to dictionary
        # print(words_dictionary[key])
        # reset values
        sentiment_list.clear()
        i = 1

    else:
        sentiment_list.append(line.split()[2])
        i += 1

# print(words_dictionary)
csv_file = open("words.csv", "w")
writer = csv.writer(csv_file)
for key, value in words_dictionary.items():
    writer.writerow([key, value])

csv_file.close()
word_file.close()


