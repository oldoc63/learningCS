# (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_one = False

#(4 * 2 <= 8) and (7 - 1 == 6)
statement_two = True

#120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher. 
def graduation_reqs(credits, gpa):
  if credits >= 120 and gpa >= 2:
    return "You meet the requirements to graduate!"

print(graduation_reqs(120,2))

