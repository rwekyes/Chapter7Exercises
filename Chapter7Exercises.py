import chapter7_rs  # Rust package for 7.9.7 and 7.9.8 -- source in chapter7_rs/

# 7.9.1 - Ask A Virtual Assistant

#def uses_any_incorrect(word, letters):
#    for letter in word.lower():
#        if letter in letters.lower():
#            return True
#        else:
#            return False     # INCORRECT!

# Ask a virtual assistant what’s wrong with this version.
# Claude Opus 5.5 had this to say

#
# Alright, alright, ALRIGHT! Everybody gather 'round! *hitches up pants*
# My name is Matt Foley, and I am a MOTIVATIONAL SPEAKER! Now I want you to
# take a good long look at this function, because I've seen a lot of code in
# my day, and let me tell ya somethin', THIS one is goin' NOWHERE!
#
# You see that loop? That loop is SUPPOSED to go through EVERY letter in the
# word! But what does it do?! It looks at ONE letter. ONE! And if that first
# letter ain't in the list, BAM! "return False!" It QUITS! It packs up its
# little bags and goes home! It doesn't even GIVE the second letter a chance!
# That's not a loop, that's a QUITTER!
#
# So you call uses_any_incorrect("banana", "n") and what do you get? FALSE!
# FALSE?! There's TWO n's in there, folks! But the 'b' came first, the 'b'
# wasn't an 'n', and the whole function just GAVE UP! *slams hand on desk*
#
# You know who gives up after one try? I'll tell you who! A guy who ends up
# thirty-five years old, eight times divorced, and LIVIN' IN A VAN DOWN BY
# THE RIVER! Eatin' government cheese! Is that what you want for your
# function?! IS IT?!
#
# Here's the deal, kiddos. "return True" inside the loop? That's FINE! The
# moment you find a match, you KNOW you're a winner, so you can go celebrate!
# But "return False"? You don't GET to say False until you've checked EVERY
# LAST LETTER and come up empty! That means you move that "return False"
# OUT of the loop, AFTER the loop, and you get rid of that else entirely:
#
def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

# NOW we're talkin'! Now that loop goes the WHOLE distance! Every letter gets
# its shot! And only when the loop has run out of letters do we finally,
# sadly, admit defeat and say False.
#
# So remember, kids: True can leave EARLY, but False has to wait until the
# very END! Otherwise you'll be livin' in a VAN! DOWN BY THE RIVER!
# *falls through coffee table*


# 7.9.2. Exercise

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('vandownbytheriver', 'xzq')
    True
    >>> uses_none('rickastley', 'goat')
    False
    """
    for letter in word.upper():
        for position in forbidden.upper():
            if letter == position:
                return False
    return True

# 7.9.3. Exercise

def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('satan','santa')
    True
    >>> uses_only('color', 'ACDLORT')
    True
    """
    for letter in word:
        if uses_none(available.upper(), letter):
            return False
    return True

# 7.9.4. Exercise

def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('funky', 'ykfnu')
    True
    >>> uses_all('geddylee','rush')
    False
    """
    for letter in required.upper():
        if uses_none(word, letter.upper()):
            return False
    return True

# 7.9.5. Exercise

def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4:
        return False

    if uses_none(word, required):
        return False

    if uses_only(word, available):
        return True

    return False


def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    score = len(word)
    if score == 4:
        return 1
    if uses_all(word, available):
        score += 7
    return score

# 7.9.6. Exercise

# I uh, kinda did that already, but I did the opposite logic with uses_none

# 7.9.7. Exercise
# More asking a virtual assistant!
# Here's what Claude Opus 5.5 had to say

# Given a function, uses_only, which takes two strings and checks that the first
# uses only the letters in the second, use it to write uses_all, which takes two
# strings and checks whether the first uses all the letters in the second,
# allowing repeats.

def uses_all_via_only(word, required):
    """Checks whether a word uses all required letters (Rust, via uses_only).

    >>> uses_all_via_only('banana', 'ban')
    True
    >>> uses_all_via_only('apple', 'api')
    False
    >>> uses_all_via_only('funky', 'ykfnu')
    True
    >>> uses_all_via_only('geddylee', 'rush')
    False
    """
    return chapter7_rs.uses_all_via_only(word, required)

# 7.9.8. Exercise

# Given a function, uses_any, which takes two strings and checks whether the first
# uses any of the letters in the second, can you use it to write uses_all, which
# takes two strings and checks whether the first uses all the letters in the second,
# allowing repeats.

def uses_all_via_any(word, required):
    """Checks whether a word uses all required letters (Rust, via uses_any).

    >>> uses_all_via_any('banana', 'ban')
    True
    >>> uses_all_via_any('apple', 'api')
    False
    >>> uses_all_via_any('funky', 'ykfnu')
    True
    >>> uses_all_via_any('geddylee', 'rush')
    False
    """
    return chapter7_rs.uses_all_via_any(word, required)
