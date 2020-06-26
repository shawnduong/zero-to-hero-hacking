# RSA

RSA (Rivest-Shamir-Adleman) is a sophisticated public-private key cryptosystem that is still widely used today for securing communications and data. RSA is largely dependent on large primes for security and relies on the fact that while it is easy to get to large primes and multiply them together, it is difficult to factor the product into the two primes that created it.

## Public-Private Key Cryptosystems

In a public-private key cryptosystem, the public encryption key is different than the private decryption key. This sort of cryptosystem allows for encryption keys to be public knowledge while never compromising the security of the encryption.

For example, Alice can generate a public and private key pair and give the public key to Bob, who will then encrypt a message using the public key. Bob can then send the message to Alice, who will use her decryption key to decrypt the message and see the plaintext. If an eavesdropper Eve were to intercept Alice's public key and Bob's encrypted message, Eve cannot decrypt Bob's message due to the fact that she is never able to intercept Alice's private key.

## Working Principles of RSA

In order to demonstrate the working principles of RSA, we will use an example.

1. RSA is reliant on two large selected primes *p* and *q*. **In real life, it is common to have primes of 1024 or 2048 bits.** For example's sake, we will use the small primes *p = 167* and *q = 239*.

2. *p* and *q* multiply together to create *n*. Therefore, *n = 167 \* 239 = 39913*.

3. Now, we need to determine how many numbers are coprime (relatively prime) with *n*. While this could be done manually, a much easier way is to use Euler's Totient Function *phi(n) = (p - 1)(q - 1)*. Therefore, *phi(39913) = (167 - 1)(239 - 1) = 39508*.

4. Now that we've determined *phi(n)*, we can compute the public key *(e, n)*. *e* needs to be a number that is coprime to *phi(n)*. In other words, *e* has to be such that *gcd(phi(n), e) = 1*. Candidates that pass this test are valid *e* values. One such candidate that satisfies this is *677*. Therefore, the public encryption key is *(677, 39913)*.

5. The private decryption key can now be computed as *d = e^-1 mod phi(n)*. Therefore, *d = 677^-1 mod 39508 = 12897*. Therefore, the private decryption key is *(12897, 39913)*.

6. Alice, having just generated the keys, gives the public key *(677, 39913)* to Bob and keeps the private key *(12897, 39913)* to herself.

7. Messages are encrypted in RSA as *c = m^e mod n*, where *c* is the ciphertext and *m* is the plaintext message. Bob wants to encrypt his message "HI", so he translates it to *7273* (ASCII) and computes *c* as *c = 7273^677 mod 39913 = 14320*. He then sends *c = 14320* back to Alice.

8. Messages are decrypted in RSA as *m = c^d mod n*. Alice receives *c = 1432* from Bob and calculates *d* as *d = 14320^12897 mod 39913 = 7273*. This translates to "HI" in ASCII. Thus, Alice and Bob have successfully used RSA to secure their communications.
