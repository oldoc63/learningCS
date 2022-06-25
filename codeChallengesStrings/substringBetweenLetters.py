# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first ocurrence of start and end in word. If start or end are not in word, the function should return word.
#For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
    starting_index = word.find(start)
    ending_index = word.find(end)
    if starting_index > -1 and ending_index > -1:
        return word[starting_index + 1:ending_index]
    return word

#Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


