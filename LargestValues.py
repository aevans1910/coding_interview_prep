# Find the k largest values in an array of n numbers. 
# Return them in a new array sorted in decreasing order.
# 
# K largest values
# Return in other array of descending open
# 1 array of n order, k largest values, return array of k

def find_largest_values(arr, k_values):
    new_arr = []
    for  values in arr:
        if len(arr) < 1:
            return None
    arr.sort(reverse = True)
    while k_values > 0:
        new_arr.append(arr[k_values-1])
        k_values -= 1
    new_arr.sort(reverse= True)
    return new_arr

print(find_largest_values([2, 5, 1, 7], 2))