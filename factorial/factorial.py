# Let see how a factorial function looks with a call stack:
def factorial(x):
    return x * factorial(x - 1) if x > 0 else 1

print(factorial(5)) 

# x == 5
# [5 * f(4)]
# [5 * [4 * f(3)]]
# [5 * [4 * [3 * f(2)]]]
# [5 * [4 * [3 * [2 * f(1)]]]]

# Each ] is a return value that is pushed to the stack during recursion,
# then recovered (wound back down) when the base case is reached.

# return 1 => 1
#      * 2 => 2
#      * 3 => 6
#      * 4 => 24
#      * 5 => 120


