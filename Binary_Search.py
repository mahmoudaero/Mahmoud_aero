'''
Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. 
Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. 
So we apply the algorithm for the left half.
'''
# Python 3 program for recursive binary search. 
# Modifications needed for the older Python 2 are found in comments. 
  
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1