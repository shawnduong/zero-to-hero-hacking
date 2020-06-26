# The Filesystem Hierarchy Standard

The typical Linux filesystem follows the **Filesystem Hierarchy Standard (FHS)**, a standard specifying a certain predictable structure that directories should follow. This is a standard set by the Linux Foundation and while distributions are not strictly required to follow it, they often do. Understanding the FHS can help a user better understand their system.

A typical system following the FHS looks like this:

```
/
|-- bin
|-- boot
|-- dev
|-- etc
|-- home
|-- lib
|-- lib64
|-- media
|-- mnt
|-- opt
|-- proc
|-- root
|-- run
|-- sbin
|-- srv
|-- sys
|-- tmp
|-- usr
`-- var
```

## `/`

The root directory from which everything else is derived from.

## `/bin`

The binary directory where program binaries and scripts are stored. Programs that you can run via the command line can typically have their code be found here, either in a binary format or in a source code format if they are reliant on an interpreter to execute. Sometimes, this is a link to `/usr/bin` instead.

## `/boot`

The boot directory that contains the files necessary for a successful system boot. In many configurations, this is a separately mounted partition in order to ensure that bootup is still possible even on an otherwise broken system.

## `/dev`

The device directory where device files can be found. Sometimes, these device files map to actual physical devices. However, this is not always the case (e.g. `/dev/null`).

## `/etc`

The etcetera directory where you can find system-wide configuration files. For example, you can find systemd configuration files here.

## `/home`

The home directory containing files belonging to regular users of a system. In many configurations, this is a separately mounted partition in order to protect user data in case the rest of the system were to somehow fail or break.

## `/lib`

The library directory containing libraries that other programs are dependent on.

## `/media`

The media directory serving as a mounting point for removable media devices such as USB drives and CD disks.

## `/mnt`

The mount directory serving as a mounting point for other filesystems.

## `/opt`

The optional directory containing optional packages.

## `/proc`

The process directory containing process and kernel files that provide information to the user and to other programs.

## `/root`

The home directory of the root user.

## `/run`

The run-time directory containing information about the current session, typically cleared at every boot.

## `/sbin`

The system binaries directory containing essential system binaries. Sometimes, this is a link to `/usr/bin` instead.

## `/srv`

The server directory containing files related to servers, such as FTP or SSH servers that might be running on your system.

## `/sys`

The system directory containing information about the computer itself, such as hardware devices and drivers.

## `/tmp`

The temporary directory containing volatile data that is cleared upon reboot.

## `/usr`

The user directory containing user programs. This is often times where the vast majority of your installed programs and their associated libraries are stored.

## `/var`

The variable directory containing often-changing data such as logs.
