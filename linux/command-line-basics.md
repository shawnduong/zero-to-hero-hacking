# Command Line Basics

While you may be used to a graphical user interface (GUI), Linux offers a very powerful command line interface (CLI). **The command line interface allows users to interact with a system through a text-based environment.** Becoming comfortable with the command line unlocks a whole new world of tools, automation, and power, and it quickly becomes obvious why the CLI is more efficient and powerful than the GUI. 

## Terminology

There's a lot of confusion between the terms **command line, shell, terminal, and console.** In fact, many users use them interchangeably although it would technically be wrong to do so. Before continuing, let's define these terms concretely.

The **terminal** or **console** is the physical device at which users can interact with systems. This is a personal computer most of the time, but not always. For example, a very powerful computer such as a mainframe can have multiple monitors/keyboards connected to it in order to serve multiple users. In this case, each physical monitor/keyboard setup could be considered a terminal because it's an endpoint.

The **command line** refers to any interface where the user interacts with the system via text and commands. A **shell** is any program that provides an interface for the user to interact with the operating system, whether it be through a command line interface or a graphical environment. In recent times and in hacker slang, a shell is most associated with its command line definition. The shell serves a command line interface, and the program that *typically* contains the shell (but not always, in the case of ttys) is referred to as a **terminal emulator**.

If you are at a computer, then you are at a *terminal* or *console*. If you have a program such gnome-terminal or urxvt open, then you have a *terminal emulator* open. This terminal emulator is running a program known as a *shell* that serves you a *command line interface*.

## Software

In order to start interacting with a command line, you first need a terminal emulator and shell. On most Linux distributions, you are most likely running GNU Bash as a shell by default. This is perhaps the most universal shell. On Linux distributions running GNOME, you are most likely running gnome-terminal as a terminal emulator by default. If you're on KDE then you might be running Konsole. You can of course always install another terminal emulator such as Terminator or st.

Ultimately, it doesn't matter what terminal emulator you use. What matters much more is what kind of shell it's serving to you. I'm personally on urxvt/Bash myself and I find this to be more than sufficient.

## Commands

A **command** is simply just an instruction. The most basic command starts off with a *utility* or *program* and can be followed by *options*, *arguments*, and/or *flags*. For example, a basic command might be:

```
$ ls -a
```

Note that `$` refers to a command being run as a non-root user, as opposed to `#` which refers to a command being run as a root user. This is **not** something that you actually type out, but is in fact just the prompt!

In this example, `ls` is the utility and `-a` is a flag. The flag is something that changes the way that the utility behaves. If we were to run `ls` with no flags, then it would not list hidden files. Because we supply `-a`, it will include hidden files.

There is no clear definition on the difference between **option, argument, and flag,** so many users use the terms interchangeably. Typically, it is understood that a **flag switches a boolean value** while an **option or argument gives input data of any other type.** For example, `-a` might be considered a flag, but `-p 80,443` might be considered an argument. Some people also refer to flags as **switches** since they switch booleans. Ultimately, the technicalities don't matter as long as you're able to communicate the same idea across.

## The Pipeline

Multiple commands can be chained together using the **pipeline**. The **pipe** operator `|` allows for the output of the command on the left to be fed into the command on the right as an input. For example, the following gets the output of `strings` and feeds it into `less`.

```
$ strings data.bin | less
```

The pipeline is a very powerful feature of \*NIX systems that allows for multiple small but simple programs to be "glued" together to form more powerful programs.

## Redirections

In addition to piping, we can do **redirections** using the `<` (feed), `>` (write), and `>>` (append) redirection operators. The **feed** operator `<` supplies the file on the right as input to the command on the left. The **write** operator `>` redirects all output that would normally go to the terminal to instead be written to a file (or file descriptor, in advanced uses). The **append** operator `>>` is similar except in that it does not overwrite preexisting content. Have a look at the following examples.

This example uses the feed operator to supply `data.txt` into the `nc` utility, effectively serving a file to all that connect to the server.

```
$ nc -l -p 6767 < data.txt
```

This example uses the write operator to write all data it receives from a `nc` session to a file called `download`, effectively downloading a file from a server (shown in the previous example).

```
$ nc 192.168.1.2 6767 > download
```

This example uses the append operator to append the output of `cat` being run on a file called `session03.log` to be appended to a file called `allsessions.log`.

```
$ cat session03.log >> allsessions.log
```

Advanced redirections using file descriptors `0` (stdin), `1` (stdout) and `2` (stderr) are also possible. For example, the following command will output all errors of a custom shell script to `/dev/null` so that they won't be printed to the screen.

```
$ ./script.sh 2> /dev/null
```

## Conclusion

These are the basics of the command line. Now that you know the concepts behind interacting with a system via the command line, you've unlocked a whole new world of tools and power use. The more you use the command line, the more you will realize that GUI interfaces are a devolution in terms of power and automation.
