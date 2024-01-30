import time
import random
import nltk
from itertools import islice
from nltk.corpus import words

nltk.download('words') # can be runned one time

def generate_random_words(num_words):
    if num_words > 10_000:
        raise ValueError("Number of words cannot exceed 10,000")

    word_list = list(set(words.words()))
    random.shuffle(word_list) # randomize
    for word in islice(word_list, num_words):
        yield word

num_words = 9_999
start_time = time.perf_counter()
for word in generate_random_words(num_words):
    print(word)

end_time = time.perf_counter()
print("Elapsed time: ", end_time - start_time)