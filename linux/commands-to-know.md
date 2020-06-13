# Commands to Know

I assume that you've already read the [command line basics](./command-line-basics.md) article to gain an understanding of what commands are and how to use them. Now that you have a basic understanding of commands, it's time to learn some common commands that you should know that are present in virtually all Linux systems you can expect to be interacting with.

## `man`

`man` is short for "manual" and is perhaps the most important command that any Linux user should know how to use. `man` will **print out the manual page for a program** (if it exists). This is useful for learning how to use a program.

Example:

```
[skat@iris:~] $ man ls
```

This will give me the manual page for the `ls` utility. Keep in mind that all commands I cover here are explained at a basic level and showing only the most basic or commonly used options. Use `man` if you would like to explore all options that a program has to offer.

## `pwd`

`pwd` is short for "print working directory" and is the first command that a lot of Linux users learn. `pwd` **will output where you currently are in the system.** *Usually*, you start out in your user home directory located somewhere in `/home/`. `pwd` can help you get oriented after you start a shell such as Bash.

Example:

```
[skat@iris:~] $ pwd
/home/skat
```

In this example, I have just opened up a terminal emulator that has started Bash by default. When I run `pwd`, I learn that I am currently located in `/home/skat`.

Note that many modern shells allow you to customize your prompt. This can include your current working directory so that you don't have to fiddle around with `pwd`. My Bash configuration, for instance, may look like the following if I'm located in `/etc/systemd/`:

```
[skat@iris:/etc/systemd] $
```

This allows me to be oriented location-wise at all times and not have to worry about `pwd`.

## `ls`

`ls` is short for "list" and is used **to list all files and subdirectories located in your current working directory.**

Example:

```
[skat@iris:~] $ ls
Documents  Downloads  Music  Pictures  VMs  Videos  Workspace
```

You can supply a location as an argument to run `ls` relative to that location. **This allows you to list the contents of other directories** without having to change directories into it.

Example:

```
[skat@iris:~] $ ls /var/log/
Xorg.0.log  Xorg.0.log.old  Xorg.1.log  Xorg.1.log.old  audit  btmp  cups  journal  lastlog  lightdm  old  pacman.log  private  tallylog  wtmp
```

A common flag that you might expect to use is `-l` (long), which will **list all contents in a long listing format** that contains more information such as permissions and sizes.

Example:

```
[skat@iris:~] $ ls -l /var/log/
total 1384
-rw-r--r--  1 root root            237978 Jun 13 05:29 Xorg.0.log
-rw-r--r--  1 root root             32654 Jun  7 17:29 Xorg.0.log.old
-rw-r--r--  1 root root             45744 Oct 22  2019 Xorg.1.log
-rw-r--r--  1 root root             32454 Oct 22  2019 Xorg.1.log.old
drwx------  2 root root              4096 Jun 22  2019 audit
-rw-rw----  1 root utmp              6912 Mar 15 01:25 btmp
drwxr-xr-x  2 root root              4096 Oct 27  2019 cups
drwxr-sr-x+ 4 root systemd-journal   4096 Oct 21  2019 journal
-rw-rw-r--  1 root utmp            292292 Dec 10  2019 lastlog
drwx--x--x  2 root lightdm           4096 Jun  8 01:01 lightdm
drwxr-xr-x  2 root root              4096 Oct  6  2019 old
-rw-r--r--  1 root root            500092 Jun  2 20:48 pacman.log
drwx------  2 root root              4096 Oct 21  2019 private
-rw-------  1 root root             64064 Jun  8 01:01 tallylog
-rw-rw-r--  1 root utmp            485760 Jun  8 01:01 wtmp
```

Another common flag that you might expect to use is `-a` (all), which will **list all contents, including hidden ones.**

Example:

```
[skat@iris:~] $ ls -a
.               .bash_history  .config   .ghidra     .lesshst  .openshot_qt         .swt          .viminfo          .xsession-errors.old  Pictures
..              .bash_logout   .dmrc     .gitconfig  .local    .pki                 .thunderbird  .vimrc            .yEd                  VMs
.BurpSuite      .bash_profile  .fehbg    .gnupg      .maltego  .putty               .tooling      .wget-hsts        .zoom                 Videos
.Xauthority     .bashrc        .fltk     .hashcat    .mozilla  .pwntools-cache-3.8  .tor-browser  .xdvirc           Documents             Workspace
.Xdefaults      .bundle        .gdbinit  .irssi      .msf4     .python_history      .urxvt        .xournalpp        Downloads
.audacity-data  .cache         .gem      .java       .note     .ssh                 .vim          .xsession-errors  Music
```

(Yes, I am aware I should clean my `/home/`.)

## `cd`

`cd` is short for "change directory" and allows you to **change your current working directory.** `cd` can be given a *relative path* or an *absolute path*. A relative path starts from your current working directory and can use `..` to denote higher directories. An absolute path starts from the root directory `/`.

Example:

```
[skat@iris:~] $ cd Music/
```

This uses a relative path (relative to `~`, i.e. my user home directory `/home/skat/`) to change directories into `Music/`. In other words, I am starting at `/home/skat/` and I want to go to `/home/skat/Music/`. `/home/skat/Music/` relative to `/home/skat/` is just `Music/`.

I can also approach this using an absolute path instead.

Example:

```
[skat@iris:~] $ cd /home/skat/Music/
```

This uses the full, *absolute* path to my `Music/` directory to change directories into it.

## `clear`

`clear` allows you to **clear your terminal emulator.** This is useful if you've just entered a whole bunch of commands and need to freshen up your workspace. Alternatively, you can sometimes use CTRL+L to achieve the same effect.

## `reset`

`reset` is similar to `clear` except it is **more thorough.** Unlike `clear` (which is essentially just printing a bunch of newline characters to "push away" junk), `reset` is a full reload. This is useful for "fixing" your interface after you've accidentally messed it up by doing something you shouldn't have.

## `cat`

`cat` is short for "concatenate" and can be used to **print one or more files out to the screen in the order that they are specified in.** `cat` will try its best to print data out in a human-readable format, although this is obviously complicated by binary files and other sorts of non-human-readable formats.

Example:

```
[skat@iris:~] $ cat .bashrc
```

This example prints out the contents of my `.bashrc` file to the screen. Because this is a human-readable file, I'm able to read its contents.

As previously mentioned, this can be used to print more than one file back-to-back in the order specified, effectively concatenating all of the contents.

Example:

```
[skat@iris:~] $ cat sess00.log sess01.log sess02.log
```

## `echo`

`echo` just **outputs its input.** This is useful for when you need to print things out to the screen or for when you need to perform redirections.

Example:

```
[skat@iris:~] $ echo "Hello there!"
Hello there!
```

This example just echoed a string back to me. I can alternatively write this to a file using redirections:

```
[skat@iris:~] $ echo "Hello there!" > output.txt
```

I can also use `echo` to print out environment variables. For example:

```
[skat@iris:~] $ echo $SHELL
/bin/bash
```

## `printenv`

Speaking of environment variables, `printenv` **prints environment variables.**

## `ps`

`ps` is short for "processes" and **lists out running processes.** By default, it only lists out running processes in the current shell that it's being run in.

Example:

```
[skat@iris:~] $ ps
    PID TTY          TIME CMD
 103562 pts/1    00:00:00 bash
 103591 pts/1    00:00:00 ps
```

A common set of flags you might find yourself using with `ps` is `aux`, which prints out all processes (`a`), all users (`u`), and includes processes not attached to a terminal (`x`). This effectively prints out all processes running on a system.

## `kill`

`kill` is a command that will take a process ID (PID) as an input and **send a SIGTERM (signal terminate) to the process, effectively telling it to clean up and cease operations.**

Example:

```
[skat@iris:~] $ kill 104042
```

This sends a SIGTERM to the process associated with the ID 104042.

A common option that you might see is `-9`, which sends a SIGKILL signal instead of a SIGTERM signal. This harshly forces the program to die instead of allowing it to cleanly terminate. This may be desirable if a program is ignoring SIGTERM signals.

Example:

```
[skat@iris:~] $ kill -9 104042
```

## `exit`

`exit` is a command that **ends the current shell session.**

## `mkdir`

`mkdir` is short for "make directory" and **creates a new directory with a given name.**

Example:

```
[skat@iris:~] $ mkdir logs/
```

This creates a directory called `logs/` relative to my current working directory. I can of course also use absolute paths if I wish.

## `touch`

`touch` can be used to create **new, empty files.**

Example:

```
[skat@iris:~] $ touch data
```

## `rmdir`

`rmdir` is short for "remove directory" and **removes an empty directory.**

Example:

```
[skat@iris:~] $ rmdir logs/
```

## `rm`

`rm` is short for "remove" and **removes files.**

Example:

```
[skat@iris:~] $ rm data
```

A common flag that you might see is `-r` which removes files recursively. **This can be used to clear out and delete directories.**

Example:

```
[skat@iris:~] $ rm -r logs/
```

Another common flag is `-f`, which forces removal. **This can be used to override any possible problems arising in file removal.** This is commonly used with `-r` to completely remove directories and their contents.

Example:

```
[skat@iris:~] $ rm -rf logs/
```

## Conclusion

These are just some of the most basic programs and utilities present on just about every Linux system. There are of course many more programs than this just list. You can have a better look at all programs available on a system for you to use by listing out `/bin/` and/or `/usr/bin/`. When in doubt, consult the `man` page.
