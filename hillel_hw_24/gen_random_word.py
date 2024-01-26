from wonderwords import RandomWord

def generate_random_words(num_words):
    if num_words > 10_000:
        raise ValueError("Number of words cannot exceed 10,000")

    r = RandomWord()
    unique_words = set()

    while len(unique_words) < num_words:
        # word = fake.word()
        word = r.word()
        if word not in unique_words:
            unique_words.add(word)
            yield word


num_words = 9_999
for word in generate_random_words(num_words):
    print(word)