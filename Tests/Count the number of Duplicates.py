#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice


# SOLUTION
def duplicate_count(text):
    a = [i for i in text.lower()]
    list_1 = {}
    counter = 0
    for i in a:
        list_1[i] = text.lower().count(i)
    for key, word in list_1.items():
        if word > 1:
            counter += 1
    return counter
