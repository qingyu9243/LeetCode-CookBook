# In a word guessing game, the player’s goal is to guess a word within a limited number of tries. After every guess, each letter is marked as a color - either green, yellow, or black. Green means the letter is both correct and in the correct position. Yellow means the letter is in the answer but the position is incorrect. Black means that the letter is not in the answer.

# Example:
# Target word:  SMILE
# Guess:        CLOSE
# Output:       BYBYG (Black, Yellow, Black, Yellow, Green)

# Given the target word and a guess, implement a function that outputs the color of each letter. Target/guess can be the length of N (not fixed to 5 letter words).

def word_guess(target, guess):
    
    target_set = set()
    for char in target:
        target_set.add(char)
    
    length = len(target)
    result = []
    
    for i in range(length):
        t_char, g_char = target[i], guess[i]
        if g_char == t_char:
            result.append("G")
        elif g_char != t_char and g_char not in target_set:
            result.append("B")
        elif g_char != t_char and g_char in target_set:
            result.append("Y")
    
    return "".join(result)
    
assert word_guess("SMILE", "CLOSE") == "BYBYG"
#assert word_guess("SMILE", "SSSSS") == "GBBBB"
#assert word_guess("SEH", "HEE") == "YGB"

# Now assume the target has repeated letters, modify your solution to accommodate for this change. When there are more instances of one letter in the guess than the target, those letters should be marked as black.

# Example:
# Target word:  HAPPY
# Guess:        PUPPY
# Output:       BBGGG (Black, Black, Green, Green, Green)
 # first        YBGGG ()
 # second       BBGGG ()

# Other examples:

# Target word:  STEEL
# Guess:        EAGER
# Output:       YBBGB (Yellow, Black, Black, Green, Black)
# first         YBBGB
# second        YBBGB

# Target word:  PANDA
# Guess:        APPLE
# Output:       YYBBB (Yellow, Yellow, Black, Black, Black)
# The second “P” in APPLE is extra, therefore it has the color black.
# first         YYYBB
# second        YYBBB
from collections import Counter

def word_guess_2(target, guess):
    
    target_dict = Counter()
    for char in target:
        target_dict[char] += 1
    
    length = len(target)
    result = []
    
    # first scan
    for i in range(length):
        t_char, g_char = target[i], guess[i]
        if g_char == t_char and target_dict[t_char] >= 1:
            result.append("G")
            target_dict[t_char] -= 1
        elif g_char != t_char and g_char not in target_dict:
            result.append("B")
        elif g_char != t_char and g_char in target_dict:
            result.append("Y")
    
    # second scan
    #print(target_dict)
    for i in range(length):
        t_char, g_char = target[i], guess[i]
        if result[i] == "Y" and target_dict[g_char] <= 0:
            result[i] = "B"
        elif result[i] == "Y" and target_dict[g_char] > 0:
            target_dict[g_char] -= 1
    #print(result)
    return "".join(result)
  
assert word_guess_2("HAPPY", "PUPPY") == "BBGGG"
assert word_guess_2("STEEL", "EAGER") == "YBBGB"
assert word_guess_2("PANDA", "APPLE") == "YYBBB"

assert word_guess_2("DANPA", "APPLE") == "YYBBB"

    
# Given a color output, a target word, and a dictionary of valid words. Find all possible valid words that match the output. If you wish, you may assume no repeated letters.

# Example:
# Target word: FORTH
# Color output: GGGGB
# Dictionary of valid words: [...."SMILE", "BUILD", "PEARL", "CLOSE", "ACTOR", "FORTY", "FORTE"….]
# Output: [FORTY, FORTE]
    
def valid_words(target, color_pattern, word_dicts):
    result = []
    for word in word_dicts:
        color_p = word_guess_2(target, word)
        if color_p == color_pattern:
            result.append(word)
            
    return result

w_dict = ["SMILE", "BUILD", "PEARL", "CLOSE", "ACTOR", "FORTY", "FORTE"]
assert valid_words("FORTH", "GGGGB", w_dict) == ["FORTY", "FORTE"]



