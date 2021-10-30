"""The analyze module uses the Flesch-Kincaid readability test to analyze text and
    produce a readability score. This score is then converted to a grade-based readability
    category. Categories range from 5th grade reading level to postgraduate.
"""

# Let's teach the program how to count syllables as best we can:
def count_syllables(words):
    """The count_syllables function takes a list of words and returns a total count
        of syllables across all words in the list.
    """
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

def count_syllables_in_word(word):
    """The count_syllables_in_word function takes a word in the form of a substring
        and returns the number of syllables. This function is based on heuristics for
        syllable counting and is about 90% accurate.
    """
    count = 0
    
    # Remove ending punctuation from each word substring
    endings = ",.;'!?:"
    last_char = word[-1]
    if last_char in endings:
        processed_word = word[:-1]
    else:
        processed_word = word
    
    # Count 1 syllable for words with <=3 letters
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
while 'word' is just the pass-through variable in that first function.
"""
def count_sentences(text):
    """The count_sentences function counts the number of sentences in a text string.
        It counts periods, semicolons, question marks, and exclamation points as terminals.
    """
    count = 0
    
    terminals = '.;!?'
    
    for char in text:
        #if char == '.' or char == '!' or char == '?' or char ==';':
        if char in terminals:
            count = count + 1
    return count

#Takes the readability score and prints the reading level it represents
def output_results(score):
    """The output_results function takes the Flesch-Kincaid score and prints out
        the corresponding reader level.
    """
    if score >= 90.0:
        print('5th grade reading level')
    elif score >= 80.0:
        print('6th grade reading level')
    elif score >= 70.0:
        print('7th grade reading level')
    elif score >= 60.0:
        print('8th-9th grade reading level')
    elif score >= 50.0:
        print('10th-12th grade reading level')
    elif score >= 30.0:
        print('College student reading level')
    else:
        print('Post-graduate reading level')

def compute_readability(text):
    """The compute_readability function takes the text string and prints out a grade-based
        readability score. It should accept strings of most sizes, though the longest string
        tested so far was five paragraphs long.
    """
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
    
    output_results(score)    # no 'print' needed - it's already expressed in function def
    
    score_values = input("Would you like to see the score values that we measured? (Y/N) ")
    score_values = score_values.upper()
    if score_values == 'Y':
        print(total_words, 'words')
        print(total_sentences, 'sentences')
        print(total_syllables, 'syllables')
        print(score, 'readability score')
    else:
        print("Thanks for analyzing!")

"""
I'm setting this program up as a module now.
By setting this conditional test below, I'm telling the
program to run the ch1text file for testing ONLY if this
is the main program.
"""

if __name__ == "__main__":
    import ch1text
    print('Chapter 1 Text:')
    compute_readability(ch1text.text)