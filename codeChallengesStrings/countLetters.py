letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#Write your unique_english_letters function here:

def unique_english_letters (word):
    unique_letters = 0
    for letter in letters:
        if letter in word:
            unique_letters += 1
    return unique_letters

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
