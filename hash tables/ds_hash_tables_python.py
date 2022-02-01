# Note: Recently, the Python programming language has made Dictionaries 
# (their Hash Tables) ordered by default! So in that language, the 
# difference between and Array (List in Python) and Hash Table (Dict in Python) are less. 
# You can read more about it here: https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/


user = {
    "age" : 54,
    "name": 'Kylie',
    "magic": True,
    "scream": lambda : print("aahhh")
}

print(user['age']) # access -> O(1)
user["spell"] = "abra kadabra" # insert -> O(1)
user["scream"]() # access -> O(1)