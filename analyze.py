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

def count_syllables_in_word(word):
    count = 0
    if len(word) <= 3: #Words w/ <=3 letters tend to be 1 syllable
        return 1
    
    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False
    
    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    
    return count

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
    
    print(total_words, 'words')
    print(total_sentences, 'sentences')

compute_readability(ch1text.text)