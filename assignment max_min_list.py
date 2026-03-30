"""
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Find the Largest and Smallest Numbers
"""
def find_min_max(numnbers):
    smallest = min(numnbers)
    largest = max(numnbers)
    return smallest, largest

#list of numbers to sort through
numbers = [3,7,9,11,13,]

smallest, largest = find_min_max(numbers)

print("numbers:", numbers)
print("smallest:", smallest)
print("largest:", largest)