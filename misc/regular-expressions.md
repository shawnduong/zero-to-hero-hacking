# Regular Expressions

> "Some people, when confronted with a problem, think: 'I know, I'll use regular expressions.' Now they have two problems."
> \- J. Zawinski

Regular expressions (also known as regex) are a **set of syntaxes used for defining search patterns.** Regular expressions are incredibly useful for quickly performing searches quickly and efficiently without the need for constructing your own search algorithms.

There are many programs, programming languages, and libraries that implement regular expressions. Ultimately, the regular expressions themselves are the same. This article will be using the `grep` utility whenever a demonstration of regular expressions in action is needed.

## Example Scenario

Let's suppose that you're working for a company called simpleSecurity. An anonymous source has just sent you a leak that's been making rounds on the darknet. You read through the leak and you find thousands of email and password combinations, and you immediately notice from the first few lines that a few of these belong to your company! The problem that you face is: how can you extract all of the leaked company credentials without having to manually sift through thousands of lines of other data? If you can efficiently find a way to quickly find out who is at risk in your company, you can notify them so that they can immediately take steps to secure their data.

The answer is regular expressions! You can use a regular expression to find email and password combinations specifically belonging to your company. Suppose that your company's email server is located at `simpleSecurity.xyz`, and a sample line from the leak looks like this:

```
someLeakedEmail@domain.com:password
```

You can use the following regular expression to quickly extract email and password combinations belonging to your company:

(Don't worry about understanding it for now.)

```
^[A-Za-z0-9_.+-]*@simpleSecurity\.xyz:.*$
```

You can use a tool such as `grep` to apply this regular expression to the leak to quickly retrieve all positive matches.

```
[skat@iris:~/Downloads] $ grep "^[A-Za-z0-9_.+-]*@simpleSecurity\.xyz:.*$" leak.txt 
johnDoe123@simpleSecurity.xyz:password123
joeDoe7777@simpleSecurity.xyz:hunter2
janeDoe123@simpleSecurity.xyz:iloveyou
```

Just so that you can get an idea of how powerful this is, there were 10k lines in the (fake and generated) leak and `grep` was able to apply the regular expression to find all matches in 0.004s. Imagine how long a human would take!

```
[skat@iris:~/Downloads] $ wc -l leak.txt 
10000 leak.txt
[skat@iris:~/Downloads] $ time grep "^[A-Za-z0-9_.+-]*@simpleSecurity\.xyz:.*$" leak.txt
johnDoe123@simpleSecurity.xyz:password123
joeDoe7777@simpleSecurity.xyz:hunter2
janeDoe123@simpleSecurity.xyz:iloveyou

real    0m0.004s
user    0m0.004s
sys     0m0.000s
```

Amazing. Let's dissect the regular expression used now. It looks really complex, but I assure you that it's actually incredibly simple once we break it down!

It first starts off with `^`. This is an anchor, and specifically it anchors our search query to the beginning of the line. The opposite of this anchor is `$`, which is an anchor that denotes the end of the line instead of the beginning. By encapsulating the rest of our expression inside of `^` and `$`, we are essentially denoting that the entire line needs to satisfy the expression in order to return a positive match.

The next part of the regular expression is `[A-Za-z0-9_.+-]`. This is a character set of valid characters that an email address might have, consisting of uppercase letters `A-Z`, lowercase letters `a-z`, numbers `0-9`, and a few special symbols `_.+-`. Putting this character set inside of `[]` means that it return a positive result for any single character that satisfies this character set. However, we need to acknowledge that an email address can have any number of characters that satisfy this. Therefore, we follow the character set with `*` which extends this character set into any number of repetitions.

The next part is `@simpleSecurity\.xyz:`. This is nothing fancy, except that we need to escape `.` to be `\.` so that the regular expression sees it as a character instead of as a symbol denoting "any character."

Finally, our regular expression ends with `.*`. `.` can mean any character, and `*` again means any number of repetitions. Thus, this returns a positive match for any password no matter what character set or length.

Putting it all together now, the regular expression as a whole can be read from left to right as: "Return a positive match for lines that start with any number of repetitions the characters found in emails, that are then followed by `@simpleSecurity.xyz:`, and are followed by any number of repetitions of any character."

Simple! Now that we've dissected one such regular expression, let's go over common elements that you can expect to be using when crafting your own regular expressions.

## Anchors

Note that this is an incomplete list and only highlights the most commonly used anchors.

| Symbol | Meaning            |
| ------ | ------------------ |
| `^`    | Start of the line. |
| `$`    | End of the line.   |
| `\A`   | Start of a string. |
| `\Z`   | End of a string.   |
| `\<`   | Start of a word.   |
| `\>`   | End of a word.     |

## Character Classes

Note that this is an incomplete list and only highlights the most commonly used character classes.

| Symbol | Meaning                      |
| ------ | ---------------------------- |
| `\c`   | Control character.           |
| `\s`   | Whitespace.                  |
| `\S`   | Non-whitespace.              |
| `\d`   | Decimal digit character.     |
| `\D`   | Non-decimal digit character. |
| `\x`   | Hexadecimal digit character. |
| `\w`   | Word.                        |
| `\W`   | Non-word.                    |

## Quantifiers

| Symbol  | Meaning                           |
| ------- | --------------------------------- |
| `*`     | 0 or more occurrences.            |
| `+`     | 1 or more occurrences.            |
| `?`     | Either 0 or 1 occurrences.        |
| `{n}`   | Exactly n occurrences.            |
| `{n,}`  | n or more occurrences.            |
| `{n,m}` | Anywhere from n to m occurrences. |

## Groups and Ranges

Note that this is an incomplete list and only highlights the most commonly used groups and ranges.

| Symbol   | Meaning                                  |
| -------- | ---------------------------------------- |
| `.`      | Any character except `\n`.               |
| `(a|b)`  | Either a or b.                           |
| `[abc]`  | Either the single characters a, b, or c. |
| `[^abc]` | Any single character but a, b, or c.     |
| `[A-Z]`  | Any single character from A to Z.        |
| `[0-9]`  | Any single digit from 0 to 9.            |
