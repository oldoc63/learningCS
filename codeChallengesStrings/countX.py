# Write a function named count_chart_x that takes a string named word and a single character named x as a parameters. The function should return the number of times x appears in word.

def count_chart_x(word, x):
    occurrences = 0
    for character in word:
        if character == x:
            occurrences += 1
    return occurrences