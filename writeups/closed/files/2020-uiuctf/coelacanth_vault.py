#!/usr/bin/python
import random
from Crypto.Util import number
from functools import reduce

TOTAL = 15
THRESHOLD = 10
MAX_COELACANTH = 9

NUM_LOCKS = 5
NUM_TRIES = 250

# substitute for math.prod
prod = lambda n: reduce(lambda x, y: x*y, n)

def create_key(t, n, size=8):
    while True:
        seq = sorted([number.getPrime(size) for _ in range(TOTAL)])
        if len(set(seq)) != len(seq):
            continue

        alpha = prod(seq[:t])
        beta = prod(seq[-t + 1:])
        if alpha > beta:
            secret = random.randint(beta, alpha)
            shares = [(secret % num, num) for num in seq]
            return secret, shares

def construct_key(shares):
    glue = lambda A, n, s=1, t=0, N=0: (n < 2 and t % N or glue(n, A % n, t, s - A//n * t, N or n), -1)[n < 1]
    mod = prod([m for s, m in shares])
    secret = sum([s * glue(mod//m, m) * mod//m for s, m in shares]) % mod
    return secret

if __name__ == "__main__":
    print("Hi, and welcome to the virtual Animal Crossing: New Horizon coelacanth vault!")
    print("There are {} different cryptolocks that must be unlocked in order to open the vault.".format(NUM_LOCKS))
    print("You get one portion of each code for each coelacanth you have caught, and will need to use them to reconstruct the key for each lock.")
    print("Unfortunately, it appears you have not caught enough coelacanths, and thus will need to find another way into the vault.")
    print("Be warned, these locks have protection against brute force; too many wrong attempts and you will have to start over!")
    print("")

    num_shares = abs(int(input("How many coelacanth have you caught? ")))
    if num_shares > MAX_COELACANTH:
        print("Don't be silly! You definitely haven't caught more than {} coelacanth!".format(MAX_COELACANTH))
        print("Come back when you decide to stop lying.")
        quit()

    for lock_num in range(NUM_LOCKS):
        print("Generating key for lock {}, please wait...".format(lock_num))
        secret, shares = create_key(THRESHOLD, TOTAL)
        r_secret = construct_key(random.sample(shares, THRESHOLD))
        assert(secret == r_secret)
        print("Generated!")
        
        print("Here are your key portions:")
        print(random.sample(shares, num_shares))

        for num_attempts in range(NUM_TRIES):
            n_secret = abs(int(input("Please input the key: ")))
            if secret == n_secret:
                print("Lock {} unlocked with {} failed attempts!".format(lock_num, num_attempts))
                break
            else:
                print("Key incorrect. You have {} tries remaining for this lock.".format(NUM_TRIES - num_attempts))        
        else:
            print("BRUTE FORCE DETECTED. LOCKS SHUT DOWN.")
            print("Get out. You don't deserve what's in this vault.")
            quit()
    
    print("Opening vault...")
    with open("flag.txt", "r") as f:
        print(f.read())
