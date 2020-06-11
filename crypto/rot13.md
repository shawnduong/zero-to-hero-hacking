# rot13

Rot13 is a **simple substitution cipher** in which letters in a plaintext alphabet are mapped to letters in a ciphertext alphabet. The ciphertext alphabet is shifted exactly 13 spaces from the plaintext alphabet. It is not important whether this shift is a positive shift or a negative shift since 13 is exactly half the size of the alphabet, meaning that both a positive shift of 13 and a negative shift of 13 result in the same ciphertext alphabet. The inverse of a rot13 is itself, meaning that applying a rot13 cipher can decrypt a rot13 ciphertext.

In order to perform a rot13, first let 'A' = 0, 'B' = 1, 'C' = 2, and so on. For every letter in the plaintext expressed as its integer counterpart *i*, its integer ciphertext counterpart can be expressed as *(i + 13) mod 26*. 'P', for example, can be expressed as 15. *(15 + 13) mod 26 = 2*. The alphabetic representation of 2 is 'C.' Therefore, 'P' becomes 'C.' This basic algorithm is applied to all characters in a plaintext sequence to create the ciphertext sequence.

As an example, the phrase "HELLO THERE" is encrypted using rot13 below.

```
H  E  L  L  O      T  H  E  R  E
07 04 11 11 14     19 07 04 17 04

(07 + 13) mod 26 = 20 => U
(04 + 13) mod 26 = 17 => R
(11 + 13) mod 26 = 24 => Y
(11 + 13) mod 26 = 24 => Y
(14 + 13) mod 26 = 01 => B

(19 + 13) mod 26 = 06 => G
(07 + 13) mod 26 = 20 => U
(04 + 13) mod 26 = 17 => R
(17 + 13) mod 26 = 04 => E
(04 + 13) mod 26 = 17 => R

URYYB GURER
```
