# Caesar Cipher

The Caesar Cipher is a **simple substitution** cipher similar to [rot13](./rot13.md) except characters are shifted *n* spaces as opposed to exactly 13 spaces.

In order to perform a Caesar Cipher with a shift of *n* spaces, first let 'A' = 0, 'B' = 1, 'C' = 2, and so on. For every letter in the plaintext, let *i* be its integer counterpart as just described. Every ciphertext character as an integer can be expressed as *(i + n) mod 26*. Cipher all plaintext characters and then join all ciphertext integers together as the characters they correspond to in order to arrive at the final ciphertext.

As an example, the phrase "HELLO THERE" is encrypted using a Caesar Cipher with *n = 5* below.

```
H  E  L  L  O      T  H  E  R  E
07 04 11 11 14     19 07 04 17 04

(07 + 5) mod 26 = 12 => M
(04 + 5) mod 26 = 09 => J
(11 + 5) mod 26 = 16 => Q
(11 + 5) mod 26 = 16 => Q
(14 + 5) mod 26 = 19 => T

(19 + 5) mod 26 = 24 => Y
(07 + 5) mod 26 = 12 => M
(04 + 5) mod 26 = 09 => J
(17 + 5) mod 26 = 22 => W
(04 + 5) mod 26 = 09 => J

MJQQT YMJWJ
```
