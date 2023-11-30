from nltk import bigrams, word_tokenize

sentence = "Natural language processing import nltkssing is fascinating."

words = word_tokenize(sentence)

bigrams_list = list(bigrams(words))

print(bigrams_list)
