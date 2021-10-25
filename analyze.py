# Analyzes text readability; part of the Readability_Test project.

import ch1text

# Let's teach the program how to count syllables as best we can:
def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        # This function applies heuristics to words
        count = count + word_count
    return count

"""
Counting syllables in words can be a nuanced, brain-driven process.
Using heuristics, we're going to teach the program how to roughly
estimate the number of syllables in a word.
"""
#process_word = word[:-1]

def count_syllables_in_word(word):
    count = 0
    
    # Remove ending punctuation from each word substring
    endings = ",.;'!?:"
    last_char = word[-1]
    if last_char in endings:
        processed_word = word[:-1]
    else:
        processed_word = word
    
    #Words w/ <=3 letters tend to be 1 syllable
    if len(processed_word) <= 3:
        return 1
    
    # Ignore silent 'e' from word endings
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]
    
    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False
    
    # Count a syllable if a consonant follows a single vowel
    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    
    # Count a syllable if word ends in y
    if processed_word[-1] in 'yY':
        count = count + 1
    
    return count

"""
Sentences = substrings that finish with ending punctuation.
The first segment of count_syllables...() creates two local variables:
word and processed_word. 'processed_word' allows us to count syllables,
while 'word' ........
"""
def count_sentences(text):
    count = 0
    
    terminals = '.;!?'
    
    for char in text:
        #if char == '.' or char == '!' or char == '?' or char ==';':
        if char in terminals:
            count = count + 1
    return count

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)
    
    # Flesch's readability algorithm to tabulate the score
    score = (206.835 - 1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllables / total_words))
    
    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')
    print(score, 'reading ease score')

compute_readability(ch1text.text)