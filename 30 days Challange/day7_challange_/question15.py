"""
Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Examples :

Input: n = 7
Output: true
Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.
Input: n = 25
Output: false
Explanation: 25 has more than two divisors: 1, 5, and 25, so it is not a prime number.
Input: n = 1
Output: false
Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.
"""
# number = int(input("Enter the number: "))

# if number >1:

#     for i in range(2,int(number**0.5)+1):
#         if number % i == 0:
#             print(f"{number} is not prime number")
#             break
#         else:
#             print(f"{number} is prime number")
# else:
#     print(f"{number}This is not prime number")
        

# Get input from the user
num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        # The else block runs only if the loop finishes without hitting 'break'
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


"""
class Solution:
    def isPrime(self, n):
        # code here
        start = 2
        end = n//2
        if n > 1:
            for x in range(start, end):
                if n%x ==0:
                    return False
            return True
        else:
            return False
"""