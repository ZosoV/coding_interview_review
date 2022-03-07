def all_subsets(given_array):

    subset = [None] * len(given_array)

    def helper(given_array, subset, i):

        if i == len(given_array):
            print(subset)
        else:
            # not adding one
            subset[i] = None
            helper(given_array, subset, i+1)

            # adding one
            subset[i] = given_array[i]
            helper(given_array, subset, i+1)
    
    return helper(given_array, subset, 0)


all_subsets([1,2])