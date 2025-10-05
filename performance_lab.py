# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3
from typing import List, Tuple, Optional
def most_frequent(numbers: List[int])->Optional[int]:
    if not numbers:
        return None
    counts = {}
    max_val=numbers[0]
    max_count=0
    for x in numbers:
        counts[x]=counts.get(x,0)+1
        if counts[x]>max_count:
            max_count=counts[x]
            max_val=x
    return max_val


"""
Time and Space Analysis for problem 1:
- Best-case: O(n)- loop goes through each item once
- Worst-case: O(n)- loop goes through each item once
- Average-case: O(n)- same as best and worst, loop goes through each item once
- Space complexity: O(n)- uses dictionary that grows wit input size
- Why this approach? counting items with a dictionary is easy and quicker
- Could it be optimized? Pretty much already is
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums: List[int])-> List[int]:
    seen=set()
    out=[]
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)- loop goes through each item once
- Worst-case: O(n)- loop goes through each item once
- Average-case: O(n)- same as best and worst, loop goes through each item once
- Space complexity: O(n)- uses set that grows with how many unique items are in the list
- Why this approach? set is easiest to track seen items and keep the first appearance in order
- Could it be optimized? Not that I can think of
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums: List[int], target: int)->List[Tuple[int, int]]:
    seen=set()
    pairs=set()
    for x in nums:
        y=target-x
        if y in seen:
            a, b=(x,y) if x<y else (y,x)
            pairs.add((a,b))
        seen.add(x)
    return list(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)- the loop still goes through each item once
- Worst-case: O(n)- the loop still goes through each item once
- Average-case: same as best and worst, loop goes through each item once
- Space complexity: O(n) - uses sets that grow with how many numbers are checked
- Why this approach? set checks complements in a simple and fast way
- Could it be optimized? Not sure
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
# THIS IS MY OPTIMIZED VERSION SINCE IT USES O(n) INSTEAD OF NESTED LOOPS.
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n: int)->List[int]:
    if n<=0:
        return []
    capacity=1
    data=[None]*capacity
    size=0
    def _resize(new_cap: int):
        nonlocal data, capacity
        print(f"Resizing from capacity={capacity} to capacity={new_cap}")
        new_data=[None]*new_cap
        for i in range(size):
            new_data[i]=data[i]
        data=new_data
        capacity=new_cap 
    for value in range(n):
        if size==capacity:
            _resize(capacity*2)
        data[size]=value
        size+=1
    return data[:size]
"""
Time and Space Analysis for problem 4:
- When do resizes happen? once the list needs more space
- What is the worst-case for a single append? O(n) as it copies all items into a bigger list
- What is the amortized time per append overall? O(1) because resizing rarely happens
- Space complexity:O(n) since the list grows with how many items are stored.
- Why does doubling reduce the cost overall? Because doubling means we don't resize every time, the work gets spread out evenly  making it faster
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums: List[int])->List[int]:
    out=[]
    s=0
    for x in nums:
        s+=x
        out.append(s)
    return out

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)-the loop still goes through each number once
- Worst-case: O(n)-same as best case
- Average-case: O(n)-same since all numbers are processed once
- Space complexity:O(n)-new list grows with input size
- Why this approach?It's simple
- Could it be optimized? Not that I can think of currently
"""
# Problem 1
if __name__ == "__main__":
    print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
    print(most_frequent([]))        
# Problem 2
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([]))
# Problem 3
print(find_pairs([1, 2, 3, 4],5))
print(find_pairs([], 10))
# Problem 4
add_n_items(6)
# Problem 5
print(running_total([1, 2, 3, 4]))
print(running_total([]))
