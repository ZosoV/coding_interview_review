#1 - Sort 10 schools around your house by distance:
# Insertion sort

#2 - eBay sorts listings by the current Bid amount:
# radix or counting sort because the Bid amount problably is bounded to an inteval,
# and are integre number

#3 - Sport scores on ESPN
# quick sort because there are some different ways to return scores
# in order to handle all these variations
# also I worried about memory, -> merge sort is O(n) increases the space complexity

#4 - Massive database (can't fit all into memory) needs to sort through past year's user data
# Merge sort -> because the data is so big I am really worried about the performance
# doesn't matter the memory usage, I want to guarantee a complexity of O(nlog(n)) in the worse case


#5 - Almost sorted Udemy review data needs to update and add 2 new reviews
# Insertion sort 
# Although this data could be massive, I am assume that most of my previous data is already
# sorted, and all I am doing is  adding 2 new reviews

#6 - Temperature Records for the past 50 years in Canada
# radix counting sort if temperature records does not have decimal places.
# Quick sort -> in memory sorting if the temperature is in decimal

#7 - Large user name database needs to be sorted. Data is very random.
# Merge sort -> if I have enough memory, is the name has name and last name, and is required
# to sorted by name-lastname, I will use merge sort or quick sort for name
# and merge sort to last name after the first sort because in this way I can guarantee
# an stability in repeated lastnames
# Quick sort ->  I am not to worried about the worst case, and the data is not massive. Also
# I can select a good pivot.

#8 - You want to teach sorting for the first time
# Buble sort, selection sort