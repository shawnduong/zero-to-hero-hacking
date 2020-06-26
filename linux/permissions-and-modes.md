# Permissions and Modes

On a Linux system, permissions and modes are essential to controlling the access of certain users and groups to files and directories. Understanding permissions and modes can help a user understand who can do what on a system, and can additionally help a user in managing the security of a system's data.

## Read, Write, Execute and Octal Modes

For any given file, there are three distinct permissions associated with it: read, write, and execute.

The **read** permission allows a user to read the file and is usually abbreviated to `r`. The **write** permission allows a user to write to the file and is usually abbreviated to `w`. The **execute** permission allows a user to execute the file and is usually abbreviated to `x`.

Each of these three permissions has a value of `r = 4`, `w = 2`, and `x = 1`, allowing every single possible combination of permissions to be expressed using only one octal digit. For example, `6` would mean read and write permissions are enabled because it's equivalent to the sum of the numerical values of read and write.

For any given file, there are three possible kinds of users associated with it: the user that owns the file, the group that owns the file, and everyone else. Permissions can be provisioned for each of these three individually in this order. Together, this forms the file's **mode**. For example, `644` would mean that the user can read and write, the group can read, and everyone else can read. `700` would mean that the user can read, write, and execute, while the group and everyone else can't do anything.

## Viewing Permissions and Modes

The `-l` flag on `ls` can be used to view all information regarding permissions about a file, including the mode, owner user, and owner group.

For example:

```
$ ls -l data.txt
-rwxr-x--- 1 skat lev1 538658 Oct 20  2019 data.txt
```

In the above example, the mode is `750`, the owner is `skat`, and the group is `lev1`. This means that the user `skat` can read, write, and execute (`7`), the group `lev1` can read and execute (`5`), and everyone else can't do anything (`0`).

## Changing Modes

`chmod` (change mode) is a useful utility that allows a user to change the mode of a file.

For example, if we wanted to change the mode of `myFile.txt` to `600`, we would use:

```
$ chmod 600 myFile.txt
```

## Changing Owners

`chown` (change owner) is another useful utility related to permissions that allows a user to change the owning user and owning group of a file.

For example, if we wanted to change the owning user of a file to `user16` and the owning group of the file `myFile.txt` to `group4`, we would use:

```
$ chown user16:group4 myFile.txt
```

## Special Permissions

Three special permissions exist: `suid`, `sgid`, and `sticky`. These three special permissions don't belong to any specific type of user and are instead prefixed to the usual 3-digit mode.

`suid` and `sgid` allows the program to set the user ID and group ID, respectively, and are denoted by `4` and `2`. For example, `6555` would mean `suid` and `sgid` enabled (`6`), and the owner, group, and all others can read and execute (`5`). This can allow a user to execute a program with temporarily elevated privileges. **This can be dangerous if your program is vulnerable to exploitation and should be avoided if you don't know what you're doing.**

`sticky` is an especially interesting special permission that prevents a file or directory from being deleted by users that have write permissions on the directory. This is most often used in the temporary directory `/tmp` to prevent users from deleting the directory itself. The sticky bit is denoted by `1`. For example, the temporary directory is often times `1777`, which means that everyone can read, write, and execute to the directory, but the sticky bit prevents them from deleting the directory itself.
