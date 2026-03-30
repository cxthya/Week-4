"""
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Sum of Numbers from 1 to n
"""

def recursive_sum(n):
    if n==1:
        return 1
    else:
        return n + recursive_sum(n-1)
    
def main():
    print("=== Recursive Sum Calculator ===")

    try:
        n= int(input("Enter a positive integer: "))
                     
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        result = recursive_sum(n)

        print(f"\nThe sum of numbers from 1 to {n} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()