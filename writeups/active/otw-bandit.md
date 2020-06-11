# OverTheWire Bandit

Welcome to OverTheWire Bandit! For many, this is their first CTF/wargame. Bandit is a beginner level wargame that teaches the basics of Linux. More specifically, it teaches you the basics of working around on a GNU/Linux system, and these skills can be generalized to more general \*NIX (Unix-like) systems.

You can access the official Bandit wargame website [here](http://overthewire.org/wargames/bandit/).

## What is Linux?

**Linux is a kernel and nothing more than that.** A kernel is a program that is at the core of an operating system and is essentially the interface between software and hardware. However, when most people say "Linux," they are actually talking about **GNU/Linux**, a family of operating systems using GNU software and a Linux kernel. This is a family of operating systems similar to how Windows 7, 8, and 10 all belong to the same family, or how macOS High Sierra, Mojave, and Catalina all belong to the same family. One key and defining feature of GNU/Linux is that it is **free/libre and open source software.** If you'd like to learn more about why that's important, there's a great TED talk by Richard Stallman that you can find [here](https://www.youtube.com/watch?v=Ag1AKIl_2GM).

The majority of the world's non-desktop systems are running on some form of Linux. These include supercomputers, servers, mainframes, and the like. While Windows is dominant in the consumer market for desktop operating systems, Linux is what powers the digital world behind the scenes. As such, it is important that we learn how to use it.

## Requirements

You will need an SSH client such as PuTTY or BSD OpenSSH. SSH (secure shell) is a protocol that allow us to remotely access a computer. We will need an SSH client in order to connect to the wargame server and start solving challenges. If you are using BSD OpenSSH, you can connect to a server using the following command:

```
$ ssh <username>@<server> -p <port>
```

If you are using another client such as PuTTY then you will need to research how to do it on your specific client. The process may be different from client to client.

## Level 0

Level 0 consists of connecting to the wargame server using SSH. Once again, you will need to research how to create an SSH connection with your specific client. However, if you are using OpenBSD (as I am in this writeup), then you can connect from your command line. The target host is `bandit.labs.overthewire.org` on port 2220 with the username `bandit0` and password `bandit0`.

```
$ ssh bandit0@bandit.labs.overthewire.org -p 2220
```

## Level 0 -> 1

This level teaches us how to read a file from the command line. We can do this using the `cat` command. The `cat` command is short for the word "concatenate" as it can be used to read multiple files back-to-back. Before reading the file, we will confirm that it exists by running `ls`, short for "list," in order to confirm that the file exists in the first place and get its filename.

```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

That's the password for the next level account, `bandit1`. We can log into the user `bandit1` now using that password. However, because `bandit1` exists on the same system that we're currently connected to, we can simply just tell the current `bandit0` connection to start an SSH connection to the user `bandit1` **on the same machine** using the special localhost IP address `127.0.0.1` which always denotes "my own machine" relative to the user.

```
bandit0@bandit:~$ ssh bandit1@127.0.0.1
```

## Level 1 -> 2

This level teaches us about special symbols. There is a file called `-` in the current directory that contains the password for the next level. If we run `ls` then we can clearly see that it exists. However, if we run `cat` then we'll see that we run into a problem due to the fact that `-` is actually special symbol.

```
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat -

```

In fact, it just pauses and we have to hit CTRL+C (keyboard interrupt) to tell the `cat` program to stop so that we can get back to our command line. What just happened?

The `-` symbol is special and can't be thought of like any other character! It denotes "standard input." In other words, we can get the output of one command and feed it as an input into another command, which isn't something that we want to do here. This is a problem for us. We want to tell the `cat` program to read a file *called* `-`, not try to read from standard input!

In order to do this, we can give a fuller name. On a Linux system `.` denotes "the current directory" and `/` denotes a directory. We can use these two to form `./-`, which means "from the current directory, talk about the `-` file." Because we are putting it in the context of the current directory, we change the meaning from "standard input" to "a file located here." We can now use `cat` to read the file just like normal.

```
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

## Level 2 -> 3

This is similar to the last two levels in that we're trying to read data from a file, but now we have a different type of scenario in which there are spaces in the filename.

```
bandit2@bandit:~$ ls
spaces in this filename
```

It would be easy for you to think that we can just use `cat` and give it `spaces in this filename` as an input, but we can very easily see that this won't work!

```
bandit2@bandit:~$ cat spaces in this filename
cat: spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filename: No such file or directory
```

Why doesn't this work? Well, because there are spaces in the filename, the `cat` program thinks that we're trying to read from four separate files named `spaces`, `in`, `this`, and `filename`, respectively. This is due to the fact that spaces separate arguments in a command. What we instead want to do is specify that `spaces in this filename` is one argument. We can do this by encapsulating the whole string in quotes.

```
bandit2@bandit:~$ cat "spaces in this filename" 
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## Level 3 -> 4

The password for the next level is located in the `inhere/` directory inside of a hidden file. First, we want to `ls` all files in the current directory to make sure that `inhere/` exists, and then we'll `cd` (change directory) into it and try to `ls` for the file containing the password.

```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
```

That's strange, there's nothing inside of `inhere/`! Well, that's not exactly what's happening. On a Linux system, files and directories starting with `.` are hidden. If we want `ls` to scan for all files and directories *including* hidden ones, we can pass the `-a` flag (a as in all). After doing so, we find the hidden file.

```
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

## Level 4 -> 5

The password for the next file is described as being the only human-readable file in the `inhere/` directory. In order to understand this level, we have to first understand what "human-readable" is to begin with.

Human-readable is exactly what it sounds like: data that can be easily interpreted by a person. This includes things like text files encoded in ASCII, or configuration files, or source code. What this doesn't include are raw data files such as binary programs, images, or the like. If we try to `cat` a non-human-readable file, the program will try its best to interpret the data and display it to us but it often times results in a huge mess that we can't understand.

In order to find out whether a file is human-readable or not, we can use the `file` command to find out what sort of data it holds. This is typically done by comparing the file's signature or magic bytes against a database of known signatures or magic bytes in order to identify its file format, if any format is identifiable to begin with.

Let's now `cd` into the `inhere/` directory and run `file` on all the files inside of it to see which ones are human-readable.

```
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls 
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```

Here, we're presented with 2 problems. First off, each file starts with a special symbol `-`. We've gone over this before in one of the previous levels, and we know that we can overcome this problem by prefixing `./`. Secondly, there are 10 files in here. While we could just run `file` 10 separate times, that would be a real pain. What we can do instead is use a **wildcard**, specifically the `*` wildcard, to denote "everything" for us. In other words, `./*` will translate to "from the current directory (`./`), I want to talk about everything (`*`)."

```
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
```

We can now see that `./-file07` is the only file of the format ASCII text, a human-readable format.

```
bandit4@bandit:~/inhere$ cat ./-file07 
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

## Level 5 -> 6

This level's description specifies that the password for the next level is stored in `inhere/` and is human-readable, 1033 bytes in size, and not executable. This is pretty clearly a problem involving usage of the `find` utility.

We can first use `find` to find a file of 1033 bytes that is not executable, and then we can use `file` to confirm that it is human-readable. The basic syntax for the command that we will be using here is:

```
$ find <directory> -size <size> ! -executable
```

Notice the `!` (not) operator. Putting it before `-executable` comes together to mean "not executable." For size, we want to specify 1033c for 1033 bytes. For the directory, we want to specify that it's somewhere in `inhere/`.

```
bandit5@bandit:~$ find inhere/ -size 1033c ! -executable
inhere/maybehere07/.file2
bandit5@bandit:~$ file inhere/maybehere07/.file2
inhere/maybehere07/.file2: ASCII text, with very long lines
bandit5@bandit:~$ cat inhere/maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

Also, as a sidenote, if you want to find out more information about how to use a utility at any time, you can read the utility's `man` (manual) page. For example, if I wanted to learn all of the ins and outs of the `find` utility, I would use:

```
$ man find
```

## Level 6 -> 7

This level's description specifies that the password file is somewhere on the server, is owned by the user `bandit7`, is owned by the group `bandit6`, and is 33 bytes in size. This is similar to the previous challenge in that we're using the `find` utility again, but it's different in that we're no longer restricted to just our home directory!

On a Linux system, `/` denotes the **root directory**. This is the uppermost directory on a system, from which all other directories are branching from. When we use the `find` command, this will be our new starting point. We will be using `-size` again, and we will also be using `-user` and `-group`. Again, you can learn more about how to use a utility by consulting its manual page.

```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c
-- snipped, a bunch of errors --
```

Whoa, we're getting a bunch of permission denied messages! This makes it difficult to find where the password is due to all of the errors we're getting. In order to filter out all of these error messages, we can **redirect** the standard error stream to a special file present in Linux systems known as `/dev/null`, which is basically a void we can throw bytes into like a trash can.

In order to understand how we can do this, we have to first understand the file descriptors on a Linux system. 0 is for standard input, 1 is for standard output, and 2 is for standard error. Because we want to redirect all error messages somewhere else (leaving behind just the standard output), we are essentially saying that we want to redirect stream 2. We can redirect all data from stream 2 to `/dev/null` using the `>` redirection operator. In other words, `2>/dev/null` means "send all errors of the command to `/dev/null`."

```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
```

After filtering out all of the error messages, we can finally see where the password for the next level is located.

```
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password 
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## Level 7 -> 8

In this level, the password is stored in a file called `data.txt` and is located next to the word "millionth." This is a `grep` problem. `grep` (globally search for regular expressions and print matching lines) is a utility that allows us to apply regular expressions to data. Usage is fairly simple in this case. We are looking for the string "millionth" in the set of data contained in `data.txt`. This will print out all lines that contain this string.

```
bandit7@bandit:~$ grep "millionth" data.txt 
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

Regular expressions can be incredibly complex but are also very powerful. In this case, it was simple. If you'd like to learn more about regular expressions, I recommend checking [this](https://www.geeksforgeeks.org/write-regular-expressions/) out.

> "Some people, when confronted with a problem, think: 'I know, I'll use regular expressions!' Now they have two problems."
> \- J. Zawinski

## Level 8 -> 9

In this level, the password is the only line of text that occurs once in `data.txt`. The obvious utility to use here is `uniq`, which prints out unique lines if you pass the `-u` flag. However, there's one catch: `uniq` is only able to print out unique lines by filtering out non-unique lines that are *adjacent to each other*. This means that we need to first sort the file in order to get all duplicate lines adjacent. We can easily do this using the `sort` utility.

This is the first challenge where we're using two utilities "glued" together to accomplish a greater task. Linux allows us to do this because it is a UNIX-like system and features something very powerful known as the **pipeline**. The pipeline allows us to **feed the output of one program to be the input of another program**. This is done using the `|` (pipe) operator. There's a great video from the AT&T archives of the UNIX operating system that has a segment where old-school hacker Brian Kernighan explains the pipeline that you can view [here](https://youtu.be/tc4ROCJYbm0?t=297).

In our case, we want to first run `sort` on the file `data.txt`. Then, we want to take its output and give that as an input into `uniq -u`. We do this by "piping" `sort` to `uniq`.

```
bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## Level 9 -> 10

For this challenge, we have a binary file `data.txt`. The password is one of the few human-readable strings that's preceded by "=" characters. This is another challenge in which we have to use the pipeline.

The `strings` utility is a tool that will try its best to extract human-readable strings from any sort of data, including binary data. We will then pipe the output of it into `grep`. In this case, the regular expression we want to be using with `grep` is `==+*`, which can be read as "an equal sign (`=`), several more occurrences of equal signs (`=+`), and then everything else that comes afterwards (`*`).

```
bandit9@bandit:~$ strings data.txt | grep "==+*"
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

## Level 10 -> 11

The password for the next level is in `data.txt`, but it's encoded in base64! First off, let's discuss what base64 is to begin with.

At a fundamental level, all data in a computer is just a bunch of 1s and 0s, also known as binary or base 2. Base 2 means that there are only two possible values that a digit can have: 0, and 1. We're used to counting in decimal, or base 10: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. Programmers might also be acquainted with hexadecimal, or base 16: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, and f. Bases are always forward-translatable and backwards-translatable, which means that a base can be translated to a higher base or a lower base (e.g. decimal to hex, or hex to binary). 

Base64 is simply just a system in which every digit can have 64 possible values. This typically consists of alphanumerics (including both upper and lower alphabetical cases) as well as a few special symbols. One thing that all Base64 schemes have are that they are *always* able to be expressed as text, which makes them very useful for transmitting data reliably over the web. Once the data has been transmitted, then it can be decomposed to the binary or other data that it encodes.

In this case, we have Base64 data and we want to perform one such decoding so that we can see what sort of data it encodes. This can be done using the `base64` utility, passing the `-d` flag to denote "decode." In addition, we have to feed it the contents of the `data.txt` file as an input. While we could just do this by running `cat` and then piping it to `base64`, there is actually another useful feature of Linux that we can use.

On a Linux system, the `<` operator means "feed as an input." We can use `< data.txt` to mean "feed the contents of `data.txt` as an input into the command."

```
bandit10@bandit:~$ base64 -d < data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## Level 11 -> 12

This one is a fun level. The password for the next level is stored in `data.txt`, but all characters have been shifted 13 spaces! This is a very simple and classic cipher known as a rot13 (rotate 13) cipher. We can see the ciphertext if we `cat` the file.

```
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
```

The easy way to solve this problem is to just copy and paste the ciphertext into an online rot13 deciphering tool, but we're going to do it the not-so-easy way to learn about a great tool called `tr` (translate).

In a rot13 cipher, the alphabet is split in half due to the fact that the alphabet is 26 characters in length. A becomes N, B becomes O, C becomes P, and so on and so forth. We can think of this as one set of characters becoming two sets of characters, so `[A-Z]` becomes `[A-M]` and `[N-Z]`. Then to apply the rotation to each character, we can use the fact that the alphabet evenly divides into two, 13-character halves and just swap the halves `[A-M]` and `[N-Z]` to become `[N-Z]` and `[A-M]` while keeping the original set of characters `[A-Z]` original. In other words, we are *translating* all `[A-Z]` to become `[N-Z]` and `[A-M]` in that order. We can do this using the `tr` tool. However, we also need to remember to do this for the lowercase counterparts of these characters, so we will include an additional set `[a-z]` that becomes `[n-z]` and `[a-m]` in that order.

When using `tr`, we can simply just group and join each set together, so all "to be translated" sets can be expressed as just `[A-Za-z]` and all "to translate into" sets can be expressed as just `[N-ZA-Mn-za-m]`. In addition, we will once again use the feed operator `<` to feed the contents of `data.txt` as an input to the `tr` utility.

```
bandit11@bandit:~$ tr '[A-Za-z]' '[N-ZA-Mn-za-m]' < data.txt 
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## Level 12 -> 13

In this level, we're going to get some practice learning how to decompress multiple types of compressions using multiple tools typically present on a \*NIX system. As the level description puts it, we have a hexdump of a file that has been repeatedly compressed. The first step we have to take is to undo the hexdump into its original binary counterpart, and then begin decompression operations.

We will likely want to be creating a temporary directory for this so that we can work inside of it. One of my favorite utilities is `mktemp`, which can create a temporary directory inside of `/tmp/` if you supply the `-d` (directory) flag. In addition, we can `cd` into the newly created temporary directory in one swift move by using an inline command. That is to say that because `mktemp -d` will print out the name of the newly generated temporary directory, and because `cd` takes a positional argument specifying which directory we would like to change into, we can have these two work in one elegant conjunction by encapsulating `mktemp -d` in `$()` inline with `cd` to denote a direct "drop-in."

```
bandit12@bandit:~$ cd $(mktemp -d)
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$
```

Beautiful. Now let's copy the contents of our home directory into our current working directory. We can do this using `~`, which is short for "my home directory." If we use this in conjunction with the `*` wildcard that we've seen before, then we can form `~/*` to mean "from my home directory, I want to talk about everything." We can copy it into our current working directory (`.`) using `cp` (copy).

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ cp ~/* .
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ ls
data.txt
```

If we `cat` the file, then we can clearly see what the level description meant when it said that the file in question is a hexdump at the outermost layer.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ cat data.txt 
00000000: 1f8b 0808 0650 b45e 0203 6461 7461 322e  .....P.^..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
00000020: 2653 598e 4f1c c800 001e 7fff fbf9 7fda  &SY.O...........
00000030: 9e7f 4f76 9fcf fe7d 3fff f67d abde 5e9f  ..Ov...}?..}..^.
00000040: f3fe 9fbf f6f1 feee bfdf a3ff b001 3b1b  ..............;.
00000050: 5481 a1a0 1ea0 1a34 d0d0 001a 68d3 4683  T......4....h.F.
00000060: 4680 0680 0034 1918 4c4d 190c 4000 0001  F....4..LM..@...
00000070: a000 c87a 81a3 464d a8d3 43c5 1068 0346  ...z..FM..C..h.F
00000080: 8343 40d0 3400 0340 66a6 8068 0cd4 f500  .C@.4..@f..h....
00000090: 69ea 6800 0f50 68f2 4d00 680d 06ca 0190  i.h..Ph.M.h.....
000000a0: 0000 69a1 a1a0 1ea0 194d 340d 1ea1 b280  ..i......M4.....
000000b0: f500 3406 2340 034d 3400 0000 3403 d400  ..4.#@.M4...4...
000000c0: 1a07 a832 3400 f51a 0003 43d4 0068 0d34  ...24.....C..h.4
000000d0: 6868 f51a 3d43 2580 3e58 061a 2c89 6bf3  hh..=C%.>X..,.k.
000000e0: 0163 08ab dc31 91cd 1747 599b e401 0b06  .c...1...GY.....
000000f0: a8b1 7255 a3b2 9cf9 75cc f106 941b 347a  ..rU....u.....4z
00000100: d616 55cc 2ef2 9d46 e7d1 3050 b5fb 76eb  ..U....F..0P..v.
00000110: 01f8 60c1 2201 33f0 0de0 4aa6 ec8c 914f  ..`.".3...J....O
00000120: cf8a aed5 7b52 4270 8d51 6978 c159 8b5a  ....{RBp.Qix.Y.Z
00000130: 2164 fb1f c26a 8d28 b414 e690 bfdd b3e1  !d...j.(........
00000140: f414 2f9e d041 c523 b641 ac08 0c0b 06f5  ../..A.#.A......
00000150: dd64 b862 1158 3f9e 897a 8cae 32b0 1fb7  .d.b.X?..z..2...
00000160: 3c82 af41 20fd 6e7d 0a35 2833 41bd de0c  <..A .n}.5(3A...
00000170: 774f ae52 a1ac 0fb2 8c36 ef58 537b f30a  wO.R.....6.XS{..
00000180: 1510 cab5 cb51 4231 95a4 d045 b95c ea09  .....QB1...E.\..
00000190: 9fa0 4d33 ba43 22c9 b5be d0ea eeb7 ec85  ..M3.C".........
000001a0: 59fc 8bf1 97a0 87a5 0df0 7acd d555 fc11  Y.........z..U..
000001b0: 223f fdc6 2be3 e809 c974 271a 920e acbc  "?..+....t'.....
000001c0: 0de1 f1a6 393f 4cf5 50eb 7942 86c3 3d7a  ....9?L.P.yB..=z
000001d0: fe6d 173f a84c bb4e 742a fc37 7b71 508a  .m.?.L.Nt*.7{qP.
000001e0: a2cc 9cf1 2522 8a77 39f2 716d 34f9 8620  ....%".w9.qm4.. 
000001f0: 4e33 ca36 eec0 cd4b b3e8 48e4 8b91 5bea  N3.6...K..H...[.
00000200: 01bf 7d21 0b64 82c0 3341 3424 e98b 4d7e  ..}!.d..3A4$..M~
00000210: c95c 1b1f cac9 a04a 1988 43b2 6b55 c6a6  .\.....J..C.kU..
00000220: 075c 1eb4 8ecf 5cdf 4653 064e 84da 263d  .\....\.FS.N..&=
00000230: b15b bcea 7109 5c29 c524 3afc d715 4894  .[..q.\).$:...H.
00000240: 7426 072f fc28 ab05 9603 b3fc 5dc9 14e1  t&./.(......]...
00000250: 4242 393c 7320 98f7 681d 3d02 0000       BB9<s ..h.=...
```

In order to reverse this hexdump which looks like it was created using the `xxd` utility, we can again just use `xxd` with a `-r` (reverse) flag to do a reverse operation. This gives us the raw binary that it originally encoded. By default, it will try to send all of this data to the standard output. We want to instead redirect its output bytes into a file that we can then analyze. We can do this using the `>` redirection operator.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ xxd -r data.txt > data_unhexdump
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data_unhexdump 
data_unhexdump: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

We can clearly see that the output data is of the type gzip. We can decompress it using `gunzip` (g-unzip). However, we first need to give it a `.gz` extension so that `gunzip` will accept its format. We can rename files using `mv` (move).

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ mv data_unhexdump data_unhexdump.gz
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ gunzip data_unhexdump.gz 
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ ls
data.txt  data_unhexdump
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data_unhexdump 
data_unhexdump: bzip2 compressed data, block size = 900k
```

Now we have bzip2 data. We can decompress it using the `bzip2` utility with the `-d` (decompress) flag.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ bzip2 -d data_unhexdump
bzip2: Can't guess original name for data_unhexdump -- using data_unhexdump.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data_unhexdump.out
data_unhexdump.out: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

We once again have gzip data. Same thing as before.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ mv data_unhexdump.out data_unhexdump.out.gz
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ gunzip data_unhexdump.out.gz 
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data_unhexdump.out 
data_unhexdump.out: POSIX tar archive (GNU)
```

Now we have a tar archive. We can use `tar` with the `xf` (extract files) argument to extract a tar archive.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ tar xf data_unhexdump.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ ls
data5.bin  data.txt  data_unhexdump.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data5.bin
data5.bin: POSIX tar archive (GNU)
```

Another tar archive. Same thing.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ tar xf data5.bin
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ ls
data5.bin  data6.bin  data.txt  data_unhexdump.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
```

Another bzip2. Same thing.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data6.bin.out
data6.bin.out: POSIX tar archive (GNU)
```

Another tar. Hopefully you're starting to get the hang of this by now.

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ tar xf data6.bin.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ ls
data5.bin  data6.bin.out  data8.bin  data.txt  data_unhexdump.out
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

You guessed it: gzip. 

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ mv data8.bin data8.bin.gz
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ gunzip data8.bin.gz 
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ file data8.bin
data8.bin: ASCII text
```

At last, we arrive at ASCII text!

```
bandit12@bandit:/tmp/tmp.NCXhmDUDrJ$ cat data8.bin 
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

## Level 13 -> 14

We're told that the password for `bandit14` is located in `/etc/bandit_pass/bandit14` and can only be read by the user `bandit14`. However, that's no problem for us because we're given the SSH key for the user `bandit14`. We can simply just use the key to log into the account instead of entering in a password. We can do this using the `-i` (identity file) flag.

```
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ file sshkey.private 
sshkey.private: PEM RSA private key
bandit13@bandit:~$ ssh -i sshkey.private bandit14@127.0.0.1
```

Just for good measure, let's also grab the password once we're logged in.

```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

## Level 14 -> 15

In order to get the password for the next level, we need to submit the current level's password to the service running on port 30000 on localhost. We can do this using `nc` (netcat), a very common networking utility. In order to connect to the service running on port 30000 on localhost (remember that localhost is `127.0.0.1`), we can just use the following command:

```
bandit14@bandit:~$ nc 127.0.0.1 30000
```

Afterwards, we can just copy and paste in the password and send it by hitting ENTER.

Alternatively, you can feed the contents of `/etc/bandit_pass/bandit14` directly into `nc` using something that should be familiar to us by now.

```
bandit14@bandit:~$ nc 127.0.0.1 30000 < /etc/bandit_pass/bandit14
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

## Level 15 -> 16

This level is similar, except now the service is located on port 30001 and is using SSL encryption. SSL (secure sockets layer) is a security standard that will require us to use some sort of SSL client now instead of `nc` like we did before.

We can use `openssl` for this. After reading the manual pages for `openssl`, it becomes apparent that we need to use `s_client` in order to create a generic SSL/TLS connection to a remote host also using SSL/TLS. The manual page for `s_client` specifies that we can connect to a remote host using `-connect host:port`. We will also use `-ign_eof` to ignore the EOF (end of file) to prevent getting messages such as "HEARTBEATING" and "Read R BLOCK" that are related to the protocol.

```
bandit15@bandit:~$ openssl s_client -connect 127.0.0.1:30001 -ign_eof < /etc/bandit_pass/bandit15
-- snipped, a bunch of data --
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

## Level 16 -> 17

This is similar to the last two levels, except now we're given a range of possible ports that the service may be residing on. We need to first find out which ports are open and then which of those open ports are speaking SSL. We can scan ports using `nmap` (network mapper), a very common tool that is a staple in any hacker's toolbox.

In `nmap`, we can specify a port range using `-p`. We can specify the ports from `31000` to `32000` using `-p31000-32000`. We can additionally get as much information as possible about them using the `-A` (as in all info) flag.

```
bandit16@bandit:~$ nmap 127.0.0.1 -p31000-32000 -A

Starting Nmap 7.40 ( https://nmap.org ) at 2020-06-11 03:01 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00028s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Not valid before: 2020-05-14T12:03:38
|_Not valid after:  2021-05-14T12:03:38
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq: 
|_    Wrong! Please enter the correct current password
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Not valid before: 2020-05-14T12:03:38
|_Not valid after:  2021-05-14T12:03:38
|_ssl-date: TLS randomness does not represent time
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.40%T=SSL%I=7%D=6/11%Time=5EE1827C%P=x86_64-pc-linux-g
SF:nu%r(GenericLines,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cu
SF:rrent\x20password\n")%r(GetRequest,31,"Wrong!\x20Please\x20enter\x20the
SF:\x20correct\x20current\x20password\n")%r(HTTPOptions,31,"Wrong!\x20Plea
SF:se\x20enter\x20the\x20correct\x20current\x20password\n")%r(RTSPRequest,
SF:31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\
SF:n")%r(Help,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x
SF:20password\n")%r(SSLSessionReq,31,"Wrong!\x20Please\x20enter\x20the\x20
SF:correct\x20current\x20password\n")%r(TLSSessionReq,31,"Wrong!\x20Please
SF:\x20enter\x20the\x20correct\x20current\x20password\n")%r(Kerberos,31,"W
SF:rong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n")%r
SF:(FourOhFourRequest,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20c
SF:urrent\x20password\n")%r(LPDString,31,"Wrong!\x20Please\x20enter\x20the
SF:\x20correct\x20current\x20password\n")%r(LDAPSearchReq,31,"Wrong!\x20Pl
SF:ease\x20enter\x20the\x20correct\x20current\x20password\n")%r(SIPOptions
SF:,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password
SF:\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 89.89 seconds
```

One of the most valuable skills a hacker can have is filter through a sea of unneeded information to find the relevant information. Here, we see a couple of interesting lines of data.

```
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo
```

We can see that 5 ports are open, 2 of them are running SSL, and 4 of them are running echo. The only port not running echo is 31790, which is also running SSL. As such, this must be the port on which the service that will give us the password to the next level resides.

```
bandit16@bandit:~$ openssl s_client -connect 127.0.0.1:31790 -ign_eof < /etc/bandit_pass/bandit16
-- snipped, a bunch of data --
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```

Here, we're given an SSH key instead of a password. Fair enough. We can use regular expressions in `grep` and give it an arbitrary overshot of the amount of lines to include after an initial match using `-A` (after), and then adjust accordingly.

```
bandit16@bandit:~$ cd $(mktemp -d)
bandit16@bandit:/tmp/tmp.x8HkE0JRxX$ openssl s_client -connect 127.0.0.1:31790 -ign_eof < /etc/bandit_pass/bandit16 2>/dev/null | grep "BEGIN RSA" -A 30
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```

Looks like my arbitrary guess of 30 was off by a bit. We'd be easily deceived into thinking that the actual number of lines to include after is 28 since we have 2 extra lines, but remember that we could give it 100 lines after and it would still give us the same result since all lines after the EOF are nonexistent. The actual number of lines needed to get from the beginning of the initial `grep` match to the end of the RSA key is in fact 26. We can then redirect that into a file.

```
bandit16@bandit:/tmp/tmp.x8HkE0JRxX$ openssl s_client -connect 127.0.0.1:31790 -ign_eof < /etc/bandit_pass/bandit16 2>/dev/null | grep "BEGIN RSA" -A 26 > ssh.key
```

Due to the nature of SSH keys, we also need to adjust their mode to be private and readable only by our own user in order to be accepted by `ssh`. We can change their access modes using `chmod` (change mode). The desired mode here is `600`, which means read and write capable for the user, and nothing else for the group or other. You can learn more about Linux modes [here](https://en.wikipedia.org/wiki/Modes_(Unix)).

```
bandit16@bandit:/tmp/tmp.x8HkE0JRxX$ chmod 600 ssh.key
bandit16@bandit:/tmp/tmp.x8HkE0JRxX$ ssh -i ssh.key bandit17@127.0.0.1
```

## Level 17 -> 18

We're given two files, `passwords.old` and `passwords.new`, and the password to the next level is the only difference between the two. We can get differences between files using the `diff` (difference) utility. Here, we want to say that we want the differences between `passwords.old` and `passwords.new`, which we can simplify to just `passwords.*` using the `*` wildcard which should be very familiar by now.

```
bandit17@bandit:~$ diff passwords.*
42c42
< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
---
> w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
```

We can see that `kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd` is inserted and `w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii` is removed. Therefore, `kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd` is the new difference between the two files and is the password to the next level.

## Level 18 -> 19

In this level, we're automatically logged out after connecting to SSH due to a modification in the `.bashrc` file. This is simple enough. We don't actually need to use an interactive and fully-fledged shell in order to execute commands through SSH. We can instead just give the command we'd like to execute directly after `ssh`. Because the `.bashrc` file has been modified, let's run `/bin/sh` to run a basic (non-Bash) shell.

```
bandit17@bandit:~$ ssh bandit18@127.0.0.1 /bin/sh
-- snipped, a bunch of data --
bandit18@127.0.0.1's password: 
whoami
bandit18
```

As we can see, we now have a basic shell and we can execute commands. Let's `cat` that `readme` file now.

```
ls
readme
cat readme
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## Level 19 -> 20

We have a SUID (set-UID) binary in the home directory that we can interact with. This looks like our first privilege escalation challenge! We can run binaries by invoking them from their path (e.g. `./bandit20-do` if we're in the same directory). Let's see what we're dealing with.

```
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
```

It looks like this allows us to run a command as the user `bandit20`. Let's run the `whois` command through this binary to confirm that we will indeed be executing commands as the user `bandit20`.

```
bandit19@bandit:~$ ./bandit20-do whoami
bandit20
```

Yup, we've successfully escalated our privileges to another user! Let's go ahead and pop a shell and get the password.

```
bandit19@bandit:~$ ./bandit20-do /bin/sh
$ cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## Level 20 -> 21

For this level, there's a SUID binary once again. However, it works a bit differently than the binary from the previous level.

```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
```

This program will firstly connect to a specific port on the localhost, and then it will receive some sort of data. If the data is the `bandit20` password, then it will transmit the `bandit21` password back.

Here, we need two sessions: one to run `suconnect`, and one to be listening for connections with `nc`. We can do this by using `screen`. You can read about `screen` usage by consulting its `man` page if you don't know how to split screens, jump terminals, or start new shells.

On one of our terminals, we will listen for connections on an arbitrary port using `nc` with the `-l -p` (listen, port) flags and giving a valid port as an argument. Additionally, we want to transmit to all connections the password for `bandit20`, which we can do using the `<` feed operator.

```
bandit20@bandit:~$ nc -l -p 6767 < /etc/bandit_pass/bandit20
```

On our other terminal, we will run `suconnect` and connect to the port that `nc` is listening to on the other terminal.

```
bandit20@bandit:~$ ./suconnect 6767
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
```

On our terminal with `nc`, we get the password to the next level.

```
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```

## Level 21 -> 22

This is the first level where we'll be exploring `cron` (chronological), which is used to schedule periodic jobs on Linux systems. We can list all cron jobs by viewing `/etc/cron.d/`.

```
bandit21@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit17_root  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  cronjob_bandit25_root
```

Based on the names, I have a feeling that `cronjob_bandit22` is the job we're looking for. Let's go ahead and read it and see what it says.

```
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

It looks like this job is running `/usr/bin/cronjob_bandit22.sh` periodically. Let's go ahead and view that script's code.

```
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

It looks like this script creates a temporary file and then reads the password for the user `bandit22` into the created temporary file. As such, all we have to do is read the file that the password is being written to.

```
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

Just as a sidenote, most systems are shifting away from cron in favor of systemd timers, a change that is controversial but that many modern hackers such as myself readily welcome (hot take).

## Level 22 -> 23

This level starts out similar to the previous one. There's a cron job that's being run periodically. Let's find it, see what script it's running, and then read the code in the script.

```
bandit22@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit17_root  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  cronjob_bandit25_root
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

Based on the cron job, we can see that this is being run as the user `bandit23`. As such, the `myname` variable inside of the shell script is equal to `bandit23`. Therefore, `mytarget` seems to be the MD5 hash generated from the string echoed in the script. We can simply just run this code in our terminal to see the output.

```
bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
```

Now we know where the `bandit23` password is being written to. We can just `cat` it from here.

```
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

## Level 23 -> 24

This is yet another level dealing with cron. Let's start the same way we started the previous two.

```
bandit23@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit17_root  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  cronjob_bandit25_root
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

```

Here, we are dealing with a much more complex script. Its functionality is summarized in the echo message: "Executing and deleting all scripts in `/var/spool/$myname`". Because this cron job is being run as the user `bandit24`, this means that it is executing and then deleting all scripts in `/var/spool/bandit24/`.

We're going to make a very simple script that writes the contents of `/etc/bandit_pass/bandit24` to a arbitrarily named file in `/tmp`, from which we can then read and get the contents.

```
bandit23@bandit:~$ vim /var/spool/bandit24/s.kat.sh; chmod +x /var/spool/bandit24/s.kat.sh
```

In case you're wondering what `chmod +x` does, it makes our script executable (change mode, add execution).

```sh
#!/bin/bash      

mkdir /tmp/s.kat./
cat /etc/bandit_pass/bandit24 > /tmp/s.kat./password
```

Now we just wait a bit for the system to get around to executing our script when it performs the cron job. After waiting for a bit, we can `cat` the password.

```
bandit23@bandit:~$ cat /tmp/s.kat./password
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

## Level 24 -> 25

In this level, we're brute forcing a 4-digit PIN checker listening on port 30002. If we enter the correct PIN, then the service will give us the password for `bandit25`. Let's give a random PIN to see what happens when we give it the wrong answer.

```
bandit24@bandit:~$ echo 1000 | nc 127.0.0.1 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Fail! You did not supply enough data. Try again.
```

Now that we know a little bit more about the program, let's try doing it again with that error message in mind.

```
bandit24@bandit:~$ bandit24=$(cat /etc/bandit_pass/bandit24); echo $bandit24 1000 | nc 127.0.0.1 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
```

Now that we know how to send a PIN, let's create a script that will attempt every single possible 4-digit PIN and write the data to a log file. We'll make a script in a temporary directory.

```
bandit24@bandit:~$ cd $(mktemp -d)
bandit24@bandit:/tmp/tmp.A0szn8VVAZ$ touch script.sh; chmod +x script.sh
bandit24@bandit:/tmp/tmp.A0szn8VVAZ$ vim script.sh
```

One useful feature of Bash (and most POSIX shells) is that we can use for loops in conjunction with a range such as `{0000..9999}` to create a wordlist that we can bruteforce with.

```sh
#!/bin/bash

# This part creates a wordlist.
bandit24=$(cat /etc/bandit_pass/bandit24)
for pin in {0000..9999}; do
    echo "$bandit24 $pin" >> wordlist
done

# This part bruteforces the service with the wordlist and logs it.
cat wordlist | nc 127.0.0.1 30002 > bruteforce.log
```

Afterwards, we run the script and read the logs.

```
bandit24@bandit:/tmp/tmp.A0szn8VVAZ$ ./script.sh
bandit24@bandit:/tmp/tmp.A0szn8VVAZ$ cat bruteforce.log
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
-- snipped, a bunch more of these --
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
```

## Level 25 -> 26

We're given the SSH key for `bandit26` but we're dropped inside of a limited shell. We need to somehow break outside of this shell jail. First, let's connect to `bandit26`.

```
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@127.0.0.1
```

Upon logging into `bandit26`, we're immediately logged out. Let's see what kind of shell it's running by having a look at `/etc/passwd` which lists user shells in addition to a bunch of other info. We'll filter out all other users using `grep`.

```
bandit25@bandit:~$ grep "bandit26" /etc/passwd
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```

It looks like `bandit26` is using a special shell: `/usr/bin/showtext`. Let's have a look at what that does.

```
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

It looks like this shell just reads `~/text.txt` using `more` and then exits. This is a very genius and not-so-obvious hack right here. The `more` utility prints information out in a pager format if there isn't enough room for all of the information to be printed right off the bat. If we were to literally shrink the size of our terminal, then `more` will page the `~/text.txt`. From here, we can gain code execution through the very limited capabilities of the `more` utility, which while limited, are enough to gain an initial foothold and spawn a traditional shell.

That said, literally *shrink your terminal* and activate the pager. From here, we can hit `v` while in the pager to pivot to a text editor such as `vim`, and from within it, we can finally pop a shell by changing the `shell` variable.

```
:set shell=/bin/bash
:shell
bandit26@bandit:~$
```

And just like that, we now have a shell!

## Level 26 -> 27

This looks like a repeat of a level we did earlier where we were given a binary program that executes commands as another user. We will use the program to spawn a shell as the user and then we can proceed from there. Again, this is a repeat of an earlier level.

```
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do /bin/sh
$ whoami
bandit27
$ cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea
```

## Level 27 -> 28

It looks like we're going to start interacting with git! Let's go ahead and clone the repository located at `ssh://bandit27-git@localhost/home/bandit27-git/repo` with the `git` utility. Remember that the git password is the same as the user password in this level.

```
bandit27@bandit:/tmp/tmp.2Jr4dMwzol$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
```

Let's get the password from the repository now.

```
bandit27@bandit:/tmp/tmp.2Jr4dMwzol$ ls
repo
bandit27@bandit:/tmp/tmp.2Jr4dMwzol$ cd repo/
bandit27@bandit:/tmp/tmp.2Jr4dMwzol/repo$ ls
README
bandit27@bandit:/tmp/tmp.2Jr4dMwzol/repo$ cat README 
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```

As a sidenote, the next few levels all have to do with git. I recommend you reading up on git before proceeding or else you'll get lost. Check [this](https://try.github.io/) out.

## Level 28 -> 29

This level starts off similar to the previous one. Let's go ahead and clone a repository and start looking for the password.

```
bandit28@bandit:~$ cd $(mktemp -d)
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN$ cd repo/
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

```

Hmm, let's see if there's anything in the git logs.

```
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN/repo$ git log
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

commit c086d11a00c0648d095d04c089786efef5e01264
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    add missing data

commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    initial commit of README.md
```

It looks like there was an info leak that got fixed. We can explore what the repository looked like before the fix by checking it out at that point in time, appropriately using `git checkout` and supplying the appropriate commit.

```
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN/repo$ git checkout c086d11a00c0648d095d04c089786efef5e01264
Note: checking out 'c086d11a00c0648d095d04c089786efef5e01264'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at c086d11... add missing data
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.TpUOfpJ7dN/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: bbc96594b4e001778eee9975372716b2

```

## Level 29 -> 30

This is yet another git challenge.

```
bandit29@bandit:~$ cd $(mktemp -d)
bandit29@bandit:/tmp/tmp.Rw9s90lO0p$ git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
bandit29@bandit:/tmp/tmp.Rw9s90lO0p$ cd repo/
bandit29@bandit:/tmp/tmp.Rw9s90lO0p/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.Rw9s90lO0p/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

```

It says that there are no passwords in production, but what about other branches? Let's see if there are any other branches that we might be interested in. We can list all branches using `git branch -a` (a as in all).

```
bandit29@bandit:/tmp/tmp.Rw9s90lO0p/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
```

Let's check out the development branch.

```
bandit29@bandit:/tmp/tmp.Rw9s90lO0p/repo$ git checkout dev
Branch dev set up to track remote branch dev from origin.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.Rw9s90lO0p/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: 5b90576bedb2cc04c86a9e924ce42faf

```

## Level 30 -> 31

This is yet another git challenge.

```
bandit30@bandit:~$ cd $(mktemp -d)
bandit30@bandit:/tmp/tmp.dvJtk8lxZo$ git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
bandit30@bandit:/tmp/tmp.dvJtk8lxZo$ cd repo/
bandit30@bandit:/tmp/tmp.dvJtk8lxZo/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.dvJtk8lxZo/repo$ cat README.md 
just an epmty file... muahaha
```

If we try any of our tactics from the previous levels, we will see that they'll only be in vain.

```
bandit30@bandit:/tmp/tmp.dvJtk8lxZo/repo$ git log
commit 3aefa229469b7ba1cc08203e5d8fa299354c496b
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:54 2020 +0200

    initial commit of README.md
bandit30@bandit:/tmp/tmp.dvJtk8lxZo/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```

The answer to this level is neither in the branches nor the logs, but actually in the tags. If we list all tags, we can see that there's a secret tag.

```
bandit30@bandit:/tmp/tmp.dvJtk8lxZo/repo$ git tag
secret
```

Let's go ahead and show this secret now.

```
bandit30@bandit:/tmp/tmp.dvJtk8lxZo/repo$ git show secret
47e603bb428404d265f59c42920d81e5
```

## Level 31 -> 32

You guessed it, yet another git problem. I'm starting to get really bored of these. Luckily, this is the last git problem.

```
bandit31@bandit:~$ ls
bandit31@bandit:~$ cd $(mktemp -d)
bandit31@bandit:/tmp/tmp.0RMRUd7BW3$ git clone ssh://bandit31-git@localhost/home/bandit31-git/repo
bandit31@bandit:/tmp/tmp.0RMRUd7BW3/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.0RMRUd7BW3/repo$ cat README.md 
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

```

It looks like this level is going to be testing our ability to push changes. If you work with git, this is something that you're probably very familiar with by now. First, we'll create  the file that will be pushed.

```
bandit31@bandit:/tmp/tmp.0RMRUd7BW3/repo$ echo "May I come in?" > key.txt
```

Then we'll add and commit it.

```
bandit31@bandit:/tmp/tmp.0RMRUd7BW3/repo$ git add -f key.txt
bandit31@bandit:/tmp/tmp.0RMRUd7BW3/repo$ git commit -m "Added key.txt."
[master 59e2100] Added key.txt.
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
```

Now all that's left is to push it.

```
bandit31@bandit:/tmp/tmp.0RMRUd7BW3/repo$ git push
Could not create directory '/home/bandit31/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 323 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: 56a9bf19c63d650ce78e6ec0354ee45e
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://bandit31-git@localhost/home/bandit31-git/repo'
```

We're finally done with all of the git stuff. Now, onto the last level!

## Level 32 -> 33

This last and final level is a jail escape. We're dropped into an uppercase shell. I love these kinds of challenges a lot. No matter what we type, our command gets translated into uppercase. This means that most things that we want to do, we can't due to the case sensitive nature of the shell.

```
>> whoami
sh: 1: WHOAMI: not found
>> printenv
sh: 1: PRINTENV: not found
>> sh
sh: 1: SH: not found
>> /bin/sh
sh: 1: /BIN/SH: not found
```

Let's see if we can find out what files are in our current directory by running `./*`, which is something that we've used before. Notice how there are zero characters that could be turned into uppercase in this string.

```
>> ./*
WELCOME TO THE UPPERCASE SHELL
```

Well, that didn't help out much. Let's speculate about how this shell works. Based off of the error messages we get whenever we enter a command, we can see that it is executing `sh`. The shell's actual code, although we can't read it, might look something like.

```
sh -c "$OUR_UPPERCASE_COMMAND"
```

On a Linux system, `$0` is a special variable that typically denotes our shell. In addition, it doesn't contain any characters that might turn into uppercase. As such, we can try to run `$0` to invoke the shell (again).

```
>> $0
$ echo $0
sh
$ whoami
bandit33
$ cat /etc/bandit_pass/bandit33
c9c3199ddf4121b10cf581a98d51caee
```

And just like that, we've completed the Bandit series!
