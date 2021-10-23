#(2 - 1 > 3) or (-5 * 2 == -10)
statement_one = True

#(9 + 5 <= 15) or (7 != 4 + 3)
statement_two = True

#Write an if statement that checks if a student either has 120 or more credits or a GPA 2.0 or higher, and if so prints:

def graduation_mailer(credits, gpa):
  if credits >= 120 or gpa >= 2:
    return "You have met at least one of the requirements."

print(graduation_mailer(110,2))
