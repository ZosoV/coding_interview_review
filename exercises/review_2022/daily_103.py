# Good morning! Here's your coding interview problem for today.

# This problem was asked by Square.

# Given a string and a set of characters, return the shortest 
# substring containing all the characters in the set.

# For example, given the string "figehaeci" and the set of 
# characters {a, e, i}, you should return "aeci".

# If there is no substring containing all the characters 
# in the set, return null.


s = "figehaeci"
characters = ["a", "e", "i"]

# Understanding:
# how many characters are allow? only lowercase letter? --> 26
# Is always a solution?
# characters could be empty?
# s could be empty?
# character have a kind of order?

# Naive solution
# characters is array_map