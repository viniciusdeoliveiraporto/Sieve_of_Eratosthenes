from math import sqrt

def is_prime(n, primes):
    if n < 2: return False
    elif n in primes: return True
    else: return False

def using_sieve(number):
    if number < 2: return []
    previous_list = [0] * (number-1)
    
    for i in range(2, number+1):
        previous_list[i-2] = i
    
    ind_previous = 0
    
    for j in range(len(previous_list)-1,-1,-1):
        if previous_list[j] % previous_list[ind_previous] == 0 and previous_list[j] != previous_list[ind_previous]:
           previous_list.pop(j)
        ind_previous += 1
        if ind_previous == len(previous_list): break
    
    return previous_list

try:
    number = int(input("Type the number: "))
    prime_numbers = using_sieve(number)
    if is_prime(number, prime_numbers):
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} isn't prime")
except ValueError:
    print("The format is wrong")
except Exception:
    print("Please, talk to me if you find an error!")
