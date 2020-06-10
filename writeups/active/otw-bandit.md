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

The password for the next level is located in the `inhere/` directory inside of a hidden file. First, we want to `ls` all files in the current directory to make sure that `inhere/` exists, and then we'll `cd` (change directory) into the it and try to `ls` for the file containing the password.

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

In order to find out whether a file is human-readable or not, we can use the `file` command to find out what sort of data it holds. This is typically done by comparing the file's signature or magic bytes against a database of known signatures or magic bytes in order to identify its file format, if any is identifiable to begin with.

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

On a Linux system `/` denotes the **root directory**. This is the uppermost directory on a system, from which all other directories are branching from. When we use the `find` command, this will be our new starting point. We will be using `-size` again, and we will also be using `-user` and `-group`. Again, you can learn more about how to use a utility by consulting its manual page.

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


